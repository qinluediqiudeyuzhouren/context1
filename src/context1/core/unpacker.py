"""
src/context1/core/unpacker.py
还原器 - 核心职责：解析聚合文档、提取文件、安全写入
[修正版 v0.2.04] 
1. 引入"叶子节点检测算法"：彻底解决 LICENSE 丢失、深层文件丢失的问题
2. 增强路径清洗：确保所有路径标准化
3. 增强 ContentPool：自动过滤递归打包产生的脏数据
"""
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional, Any
from context1.utils.fs import safe_write_file

# 正则匹配模式
MD_PATTERN = re.compile(r'^--- 文件: (.+?) ---$')
XML_PATTERN = re.compile(r'<document path="(.+?)">')
PYTHON_BUNDLE_PATTERN = re.compile(r'# <ctx1:file path="(.+?)">')

def parse_document(content: str) -> List[Dict[str, str]]:
    # 统一换行符
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    lines = content.split('\n')
    files = []
    
    current_file = None
    current_content = []
    format_type = None
    
    for line in lines:
        if not format_type:
            if MD_PATTERN.match(line): format_type = 'markdown'
            elif XML_PATTERN.match(line): format_type = 'xml'
            elif PYTHON_BUNDLE_PATTERN.match(line): format_type = 'python-bundle'
        
        matched_header = False
        new_file_path = None

        if format_type == 'markdown':
            match = MD_PATTERN.match(line)
            if match: new_file_path = match.group(1).strip(); matched_header = True
        elif format_type == 'xml':
            match = XML_PATTERN.match(line)
            if match: new_file_path = match.group(1).strip(); matched_header = True
        elif format_type == 'python-bundle':
            match = PYTHON_BUNDLE_PATTERN.match(line)
            if match: new_file_path = match.group(1).strip(); matched_header = True
            if current_file and line.strip() == '# </ctx1:file>':
                files.append({'path': current_file, 'content': '\n'.join(current_content)})
                current_file = None; current_content = []
                continue

        if matched_header:
            if current_file: files.append({'path': current_file, 'content': '\n'.join(current_content)})
            current_file = new_file_path; current_content = []
            continue
         
        if current_file:
            if format_type == 'xml' and line.strip() == '</document>': continue
            current_content.append(line)
            
    if current_file: files.append({'path': current_file, 'content': '\n'.join(current_content)})
    return files

class ContentPool:
    def __init__(self, files: List[Dict[str, str]]):
        self.pool: Dict[str, List[Tuple[str, str]]] = {}
        self.seen_paths = set()
        
        for file_data in files:
            raw_path = file_data['path']
            if raw_path.startswith("./"): raw_path = raw_path[2:]
            
            # 过滤脏数据 (防止递归打包的产物混入)
            if ".ctx1" in raw_path and "/" in raw_path: continue
            if raw_path in self.seen_paths: continue
            
            self.seen_paths.add(raw_path)
            filename = Path(raw_path).name
            if filename not in self.pool: self.pool[filename] = []
            self.pool[filename].append((raw_path, file_data['content']))
    
    def get_file(self, filename: str) -> Optional[Tuple[str, str]]:
        if filename in self.pool and len(self.pool[filename]) == 1: return self.pool[filename][0]
        return None
    
    def get_all_files(self, filename: str) -> List[Tuple[str, str]]:
        return self.pool.get(filename, [])

def parse_layout_tree(tree_content: str, format_type: str = "simple") -> List[str]:
    if "├──" in tree_content or "└──" in tree_content or "│" in tree_content:
        return parse_ascii_tree(tree_content)
    return parse_simple_tree(tree_content)

def parse_simple_tree(tree_content: str) -> List[str]:
    target_paths = []
    lines = tree_content.strip().split('\n')
    dir_stack = []
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith('#'): continue
        indent_level = len(line) - len(line.lstrip())
        while len(dir_stack) > indent_level // 2: dir_stack.pop()
        line_content = stripped_line
        if line_content.endswith('/'):
            dir_stack.append(line_content.rstrip('/'))
        else:
            file_path = '/'.join(dir_stack + [line_content]) if dir_stack else line_content
            if file_path.startswith('./'): file_path = file_path[2:]
            target_paths.append(file_path)
    return target_paths

def parse_ascii_tree(tree_content: str) -> List[str]:
    """
    [核心算法升级] 解析 ASCII 树
    使用 Lookahead (向前看) 策略来判断是否为叶子节点(文件)
    """
    target_paths = []
    lines = tree_content.strip().split('\n')
    
    # 状态变量: (depth, full_path)
    last_node = None 
    
    path_stack = []
    # 匹配: 前缀(Group1), 连接符(Group2), 名称(Group3)
    pattern = re.compile(r'^([│ ]*)(├── |└── )(.+)')
    
    for line in lines:
        line = line.rstrip()
        # 跳过空行、注释、根目录点
        if not line or line.startswith('#') or line == ".": continue

        match = pattern.match(line)
        if match:
            indent_prefix = match.group(1)
            name = match.group(3).strip()
            
            # 计算当前深度 (标准格式通常是4个字符一级)
            depth = len(indent_prefix) // 4
            
            # --- 🍃 叶子节点判定逻辑 ---
            # 如果上一个节点存在，我们需要判断它是不是目录。
            # 如果【当前行】的深度 > 【上一行】的深度，说明上一行是这一行的父级(目录)。
            # 如果【当前行】的深度 <= 【上一行】的深度，说明上一行没有子节点了，它是一个文件(叶子)。
            if last_node:
                last_depth, last_path = last_node
                if depth <= last_depth:
                    # 上一个节点是叶子，加入目标列表
                    target_paths.append(last_path)
            # ---------------------------

            # 调整栈：现在的栈应该保留 depth 个父级
            while len(path_stack) > depth: path_stack.pop()
            
            # 构建当前路径
            current_full_path = "/".join(path_stack + [name])
            
            # 清洗路径
            clean_path = current_full_path
            if clean_path.startswith("./"): clean_path = clean_path[2:]
            
            # 更新状态
            path_stack.append(name)
            last_node = (depth, clean_path)
    
    # 循环结束后，最后一个节点肯定是叶子节点
    if last_node:
        target_paths.append(last_node[1])
            
    return target_paths

def calculate_path_similarity(path1: str, path2: str) -> int:
    """过滤 . 组件"""
    p1_parts = [p for p in Path(path1).parts if p != '.']
    p2_parts = [p for p in Path(path2).parts if p != '.']
    similarity = 0
    for p1, p2 in zip(p1_parts, p2_parts):
        if p1 == p2: similarity += 1
        else: break
    if p1_parts and p2_parts and p1_parts[-1] != p2_parts[-1]: return -1
    return similarity

def resolve_target(target_path: str, content_pool: ContentPool) -> Tuple[str, Any]:
    if target_path.startswith("./"): target_path = target_path[2:]
    filename = Path(target_path).name
    
    unique_file = content_pool.get_file(filename)
    if unique_file: return 'match', unique_file[1]
    
    candidates = content_pool.get_all_files(filename)
    if not candidates: return 'scaffold', f"# TODO: Generated by Context1 scaffold for {filename}"

    best_match = None
    max_score = -1
    conflict_list = []
    
    for cand_path, cand_content in candidates:
        score = calculate_path_similarity(target_path, cand_path)
        if score == -1: continue
        if score > max_score:
            max_score = score
            best_match = (cand_path, cand_content)
            conflict_list = [(cand_path, cand_content)]
        elif score == max_score:
            conflict_list.append((cand_path, cand_content))
            
    if len(conflict_list) > 1:
        debug_info = "\n".join([f"# - {p}" for p, _ in conflict_list])
        return 'conflict', f"# Conflict resolution for {target_path}\n# Candidates:\n{debug_info}"
    
    if best_match: return 'match', best_match[1]
    return 'scaffold', f"# TODO: Generated by Context1 scaffold for {filename}"

def unpack_project(source_file: Path, output_dir: Path, force: bool = False, structure_only: bool = False, tree_path: Optional[Path] = None, dry_run: bool = False) -> Dict[str, int]:
    if not source_file.exists(): raise FileNotFoundError(f"Source file not found: {source_file}")
    try: content = source_file.read_text(encoding='utf-8')
    except UnicodeDecodeError: content = source_file.read_text(encoding='latin-1')
    
    files = parse_document(content)
    content_pool = ContentPool(files)
    stats = {"match": 0, "scaffold": 0, "conflict": 0, "failed": 0, "success": 0, "skipped": 0}
    
    if tree_path and tree_path.exists():
        tree_content = tree_path.read_text(encoding='utf-8')
        # 自动检测并解析
        target_paths = parse_layout_tree(tree_content)
        
        if not dry_run:
            output_dir.mkdir(parents=True, exist_ok=True)

        for target_path in target_paths:
            status, result_content = resolve_target(target_path, content_pool)
            if dry_run:
                stats[status] += 1
                continue
            try:
                full_path = output_dir / target_path
                if status == 'conflict':
                    full_path = full_path.with_suffix(full_path.suffix + ".CONFLICT")
                    stats['conflict'] += 1
                elif status == 'scaffold': stats['scaffold'] += 1
                else: stats['match'] += 1
                
                full_path.parent.mkdir(parents=True, exist_ok=True)
                
                if status == 'conflict' or not full_path.exists() or force:
                    full_path.write_text(result_content, encoding='utf-8')
                else:
                    if status == 'match': stats['match'] -= 1; stats['skipped'] += 1
            except Exception as e:
                print(f"Error writing {target_path}: {e}")
                stats['failed'] += 1
    else:
        if dry_run: stats['match'] = len(files); return stats
        for file_data in files:
            rel_path = file_data['path']
            if rel_path.startswith('./'): rel_path = rel_path[2:]
            try:
                written = safe_write_file(output_dir, rel_path, file_data['content'], force=force)
                if written: stats['success'] += 1
                else: stats['skipped'] += 1
            except Exception: stats['failed'] += 1
    return stats