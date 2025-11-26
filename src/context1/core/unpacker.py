"""
src/context1/core/unpacker.py
还原器 - 核心职责：解析聚合文档、提取文件、安全写入
[修正版] 修复了 Python 缩进错误，优化了 strip 逻辑以保护数据完整性
[新增] 支持 Python Bundle 格式、智能内容池、结构树驱动重构
"""
import re
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from context1.utils.fs import safe_write_file

MD_PATTERN = re.compile(r'^--- 文件: (.+?) ---$')
XML_PATTERN = re.compile(r'<document path="(.+?)">')
PYTHON_BUNDLE_PATTERN = re.compile(r'# <ctx1:file path="(.+?)">')

def parse_document(content: str) -> List[Dict[str, str]]:
    """
    解析文档内容，返回文件列表
    支持三种格式：Markdown、XML、Python Bundle
    """
    # 统一换行符为 \n
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    lines = content.split('\n')
    files = []
    
    current_file = None
    current_content = []
    format_type = None  # 'markdown', 'xml', 'python-bundle'
    
    for line in lines:
        # 检测格式类型
        if not format_type:
            if MD_PATTERN.match(line):
                format_type = 'markdown'
            elif XML_PATTERN.match(line):
                format_type = 'xml'
            elif PYTHON_BUNDLE_PATTERN.match(line):
                format_type = 'python-bundle'
        
        # Markdown Header Match
        if format_type == 'markdown':
            md_match = MD_PATTERN.match(line)
            if md_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = md_match.group(1).strip()
                current_content = []
                continue
                
        # XML Header Match
        elif format_type == 'xml':
            xml_match = XML_PATTERN.match(line)
            if xml_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = xml_match.group(1).strip()
                current_content = []
                continue
        
        # Python Bundle Header Match
        elif format_type == 'python-bundle':
            bundle_match = PYTHON_BUNDLE_PATTERN.match(line)
            if bundle_match:
                if current_file:
                    files.append({
                        'path': current_file,
                        'content': '\n'.join(current_content)
                    })
                current_file = bundle_match.group(1).strip()
                current_content = []
                continue
            
            # Python Bundle Footer Match
            if current_file and line.strip() == '# </ctx1:file>':
                files.append({
                    'path': current_file,
                    'content': '\n'.join(current_content)
                })
                current_file = None
                current_content = []
                continue
         
        # Content Collection
        if current_file:
            if format_type == 'xml' and line.strip() == '</document>':
                continue
            # 保持原始缩进，不进行额外处理
            current_content.append(line)
            
    # Save last file
    if current_file:
        files.append({
            'path': current_file,
            'content': '\n'.join(current_content)
        })
        
    return files

class ContentPool:
    """
    智能内容池 - 解决重名文件问题
    """
    def __init__(self, files: List[Dict[str, str]]):
        self.pool: Dict[str, List[Tuple[str, str]]] = {}
        
        # 填充内容池
        for file_data in files:
            filename = Path(file_data['path']).name
            if filename not in self.pool:
                self.pool[filename] = []
            self.pool[filename].append((file_data['path'], file_data['content']))
    
    def get_file(self, filename: str) -> Optional[Tuple[str, str]]:
        """
        获取指定文件名的文件内容
        返回：(原始路径, 内容)
        """
        if filename in self.pool and len(self.pool[filename]) == 1:
            return self.pool[filename][0]
        return None
    
    def get_all_files(self, filename: str) -> List[Tuple[str, str]]:
        """
        获取所有同名文件
        """
        return self.pool.get(filename, [])

def parse_layout_tree(tree_content: str) -> List[str]:
    """
    解析布局树文件
    返回：目标路径列表
    """
    target_paths = []
    lines = tree_content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # 处理缩进
        if line.startswith('  '):
            # 去掉缩进，保留相对路径
            line = line[2:]
        
        # 目录以 / 结尾，文件不以 / 结尾
        if line.endswith('/'):
            # 目录，跳过处理（只处理文件）
            continue
        else:
            # 文件，确保路径格式正确
            if not line.startswith('./'):
                line = './' + line
            target_paths.append(line)
    
    return target_paths

def calculate_path_similarity(path1: str, path2: str) -> int:
    """
    计算两个路径的相似度
    返回：重叠的目录层级数量
    """
    parts1 = Path(path1).parts
    parts2 = Path(path2).parts
    
    similarity = 0
    for i, (p1, p2) in enumerate(zip(parts1, parts2)):
        if p1 == p2:
            similarity += 1
        else:
            break
    
    return similarity

def resolve_target(target_path: str, content_pool: ContentPool) -> Tuple[str, str]:
    """
    解析目标路径对应的文件内容
    返回：(状态, 内容或错误信息)
    状态: 'match', 'scaffold', 'conflict'
    """
    filename = Path(target_path).name
    
    # Step 1: 检查唯一匹配
    unique_file = content_pool.get_file(filename)
    if unique_file:
        return 'match', unique_file
    
    # Step 2: 路径相似度匹配
    candidates = content_pool.get_all_files(filename)
    if candidates:
        best_match = None
        best_similarity = -1
        best_matches = []
        
        for candidate_path, candidate_content in candidates:
            similarity = calculate_path_similarity(target_path, candidate_path)
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = (candidate_path, candidate_content)
                best_matches = [(candidate_path, candidate_content)]
            elif similarity == best_similarity:
                # 相似度相同，添加到候选列表
                best_matches.append((candidate_path, candidate_content))
        
        # 如果有多个最佳匹配，产生冲突
        if len(best_matches) > 1:
            return 'conflict', f"Multiple candidates with same similarity: {best_matches}"
        elif best_match:
            return 'match', best_match
    
    # Step 3: 特殊处理 __init__.py
    if filename == '__init__.py':
        return 'scaffold', f"# TODO: Generated by Context1 scaffold for {filename}"
    
    # Step 4: 脚手架
    return 'scaffold', f"# TODO: Generated by Context1 scaffold for {filename}"

def unpack_project(
    source_file: Path,
    output_dir: Path,
    force: bool = False,
    structure_only: bool = False,
    tree_path: Optional[Path] = None,
    dry_run: bool = False
) -> Dict[str, any]:
    """
    执行还原操作
    支持重构模式和试运行模式
    """
    if not source_file.exists():
        raise FileNotFoundError(f"Source file not found: {source_file}")
        
    # 尝试不同的编码读取文件
    content = ""
    for encoding in ['utf-8', 'utf-8-sig', 'utf-16', 'latin-1']:
        try:
            content = source_file.read_text(encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    
    if not content:
        raise UnicodeDecodeError(f"无法解码文件: {source_file}")
    
    files = parse_document(content)
    
    # 创建内容池
    content_pool = ContentPool(files)
    
    # 检查是否为重构模式
    refactor_mode = tree_path is not None and tree_path.exists()
    
    if refactor_mode:
        # 重构模式：使用结构树
        tree_content = tree_path.read_text(encoding='utf-8')
        target_paths = parse_layout_tree(tree_content)
        
        stats = {
            "create": 0, "match": 0, "scaffold": 0, "conflict": 0,
            "skipped": 0, "failed": 0
        }
        
        # 检查目标目录是否为空
        if not dry_run and not force and any(output_dir.iterdir()):
            raise ValueError(f"目标目录 {output_dir} 不为空，请使用 --force 强制覆盖")
        
        for target_path in target_paths:
            status, content_or_error = resolve_target(target_path, content_pool)
            
            try:
                if dry_run:
                    # 试运行模式：只记录不写入
                    if status == 'match':
                        stats["match"] += 1
                    elif status == 'scaffold':
                        stats["scaffold"] += 1
                    elif status == 'conflict':
                        stats["conflict"] += 1
                else:
                    # 实际执行
                    if status == 'match':
                        written = safe_write_file(output_dir, target_path, content_or_error, force=force)
                        if written:
                            stats["match"] += 1
                        else:
                            stats["skipped"] += 1
                    elif status == 'scaffold':
                        # 创建脚手架文件
                        scaffold_path = output_dir / target_path
                        scaffold_path.parent.mkdir(parents=True, exist_ok=True)
                        scaffold_path.write_text(content_or_error, encoding='utf-8')
                        stats["scaffold"] += 1
                    elif status == 'conflict':
                        # 创建冲突文件
                        conflict_path = output_dir / f"{target_path}.CONFLICT"
                        conflict_path.parent.mkdir(parents=True, exist_ok=True)
                        
                        # 获取所有候选路径
                        candidates = content_pool.get_all_files(Path(target_path).name)
                        conflict_content = f"# Conflict resolution for {target_path}\n"
                        conflict_content += f"# Original candidates:\n"
                        for candidate_path, _ in candidates:
                            conflict_content += f"# - {candidate_path}\n"
                        
                        conflict_path.write_text(conflict_content, encoding='utf-8')
                        stats["conflict"] += 1
                        
            except Exception as e:
                if dry_run:
                    stats["failed"] += 1
                else:
                    print(f"❌ Error processing {target_path}: {e}")
                    stats["failed"] += 1
        
        return stats
    else:
        # 普通模式：直接还原
        stats = {"success": 0, "skipped": 0, "failed": 0}
        
        for file_data in files:
            rel_path = file_data['path']
            file_content = file_data['content']
            
            try:
                if structure_only:
                    file_content = ""
                 
                written = safe_write_file(output_dir, rel_path, file_content, force=force)
                
                if written:
                    stats["success"] += 1
                else:
                    stats["skipped"] += 1
                    
            except Exception as e:
                print(f"❌ Error unpacking {rel_path}: {e}")
                stats["failed"] += 1
                
        return stats

