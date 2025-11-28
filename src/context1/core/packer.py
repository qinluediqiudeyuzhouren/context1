"""
src/context1/core/packer.py
打包器 - 核心职责：生成目录树、文件排序、格式化输出(Markdown/XML/Python Bundle)
[修正版] 增加了内存溢出保护 (Pre-read size check)
"""
import re
from pathlib import Path
from typing import List, Dict, Any, Tuple
from datetime import datetime
from context1.core.config import Config, SortStrategy, OutputFormat

def calculate_dslpp_weight(filename: str, weights: List[Dict[str, Any]]) -> int:
    """
    计算 DS-LPP 权重
    Args:
        filename: 文件名
        weights: 权重配置列表
    Returns:
        权重值，未匹配则返回默认值 50
    """
    import fnmatch
    
    # 首先检查 test 文件，因为它有最高优先级
    if filename.startswith("test_") and filename.endswith(".py"):
        for weight_config in weights:
            if weight_config["pattern"] == "test_*.py":
                return weight_config["weight"]
    
    for weight_config in weights:
        pattern = weight_config["pattern"]
        weight = weight_config["weight"]
        
        # 跳过 test 模式，因为已经处理过了
        if pattern == "test_*.py":
            continue
            
        # 使用 fnmatch 进行 glob 模式匹配
        if fnmatch.fnmatch(filename, pattern):
            return weight
        # 额外处理一些特殊情况
        elif pattern == "*_ent.py" and filename.endswith("_entity.py"):
            return weight
        elif pattern == "*_d.py" and filename.endswith("_d.py"):
            return weight
        elif pattern == "*_i.py" and filename.endswith("_i.py"):
            return weight
        elif pattern == "*_c.py" and filename.endswith("_c.py"):
            return weight
        elif pattern == "*_bhv.py" and filename.endswith("_bhv.py"):
            return weight
        elif pattern == "*_u.py" and (filename.endswith("_u.py") or filename.endswith("_service.py")):
            return weight
        elif pattern == "*_stg.py" and filename.endswith("_stg.py"):
            return weight
        elif pattern == "*_s.py" and (filename.endswith("_s.py") or filename.endswith("_service.py")):
            return weight
        elif pattern == "*_cmd.py" and filename.endswith("_cmd.py"):
            return weight
    
    return 50  # 默认权重

def vscode_sort_key(file_path: Path) -> List[str]:
    """
    【核心特色】VSCode 风格自然排序
    """
    parts = file_path.parts
    sort_parts = []
    
    for i, part in enumerate(parts):
        # 简单模拟：点开头优先级最高(0)，其他(1)
        priority = 0 if part.startswith('.') else 1
        sort_parts.append((priority, part.lower()))
    
    return sort_parts

def sort_files(files: List[Path], config: Config) -> List[Path]:
    """
    根据配置的排序策略对文件进行排序
    """
    root = config.project_root
    
    if config.sort_strategy == SortStrategy.NAME:
        # 默认按名称排序
        return sorted(files, key=lambda f: f.relative_to(root))
    elif config.sort_strategy == SortStrategy.VSCODE:
        # VSCode 风格排序
        return sorted(files, key=lambda f: vscode_sort_key(f.relative_to(root)))
    elif config.sort_strategy == SortStrategy.DSLPP:
        # DS-LPP 拓扑排序
        def dslpp_sort_key(file_path: Path) -> Tuple[int, str]:
            try:
                rel_path = file_path.relative_to(root)
                filename = rel_path.name
            except ValueError:
                # 如果无法获取相对路径，使用文件名本身
                filename = file_path.name
            weight = calculate_dslpp_weight(filename, config.dslpp_weights)
            return (weight, filename)
        
        return sorted(files, key=dslpp_sort_key)
    else:
        # 默认回退到名称排序
        return sorted(files, key=lambda f: f.relative_to(root))

def extract_metadata(file_path: Path) -> Dict[str, str]:
    """
    提取文件元数据（@Role 和 @Responsibility）
    Args:
        file_path: 文件路径
    Returns:
        包含 role 和 responsibility 的字典
    """
    metadata = {"role": "", "responsibility": ""}
    
    try:
        # 读取文件前 20 行
        lines = file_path.read_text(encoding='utf-8', errors='ignore').split('\n')[:20]
        
        # 正则匹配 @Role 和 @Responsibility，支持多行格式
        role_pattern = re.compile(r'@Role:\s*(.*?)(?:\n|$)')
        responsibility_pattern = re.compile(r'@Responsibility:\s*(.*?)(?:\n|$)')
        
        for line in lines:
            role_match = role_pattern.search(line)
            if role_match and not metadata["role"]:
                metadata["role"] = role_match.group(1).strip()
            
            responsibility_match = responsibility_pattern.search(line)
            if responsibility_match and not metadata["responsibility"]:
                metadata["responsibility"] = responsibility_match.group(1).strip()
                
    except Exception:
        # 如果读取失败，返回空元数据
        pass
    
    return metadata

def generate_layout_tree(files: List[Path], root: Path) -> str:
    """
    生成布局蓝图文件（纯文本树格式）
    目录名必须以 / 结尾
    """
    tree_lines = []
    
    # 过滤掉噪音文件
    filtered_files = []
    for file_path in files:
        rel_path = file_path.relative_to(root)
        # 排除 __init__.py, __pycache__ 等
        if (rel_path.name != "__init__.py" and 
            "__pycache__" not in rel_path.parts and
            not rel_path.name.startswith(".")):
            filtered_files.append(file_path)
    
    # 按目录分组
    dir_structure = {}
    for file_path in filtered_files:
        rel_path = file_path.relative_to(root)
        dir_path = rel_path.parent
        
        # 确保目录以 / 结尾
        dir_key = str(dir_path) + "/" if dir_path != Path(".") else "./"
        if dir_key not in dir_structure:
            dir_structure[dir_key] = []
        dir_structure[dir_key].append(rel_path.name)
    
    # 生成树结构
    for dir_key in sorted(dir_structure.keys()):
        tree_lines.append(dir_key)
        for filename in sorted(dir_structure[dir_key]):
            tree_lines.append(f"  {filename}")
    
    return "\n".join(tree_lines)

def generate_tree(files: List[Path], root: Path, format_type: str = "ascii") -> str:
    """生成目录树结构
    Args:
        files: 文件列表
        root: 根目录
        format_type: 格式类型 ("simple" 或 "ascii")
    """
    if format_type == "ascii":
        return generate_ascii_tree(files, root)
    else:
        return generate_simple_tree(files, root)

def generate_simple_tree(files: List[Path], root: Path) -> str:
    """生成简单的目录树结构（当前格式）"""
    tree_lines = ["# Project Structure"]
    
    # 过滤掉噪音文件
    filtered_files = []
    for file_path in files:
        rel_path = file_path.relative_to(root)
        # 排除 __init__.py, __pycache__ 等
        if (rel_path.name != "__init__.py" and
            "__pycache__" not in rel_path.parts and
            not rel_path.name.startswith(".")):
            filtered_files.append(file_path)
    
    # 按目录分组
    dir_structure = {}
    for file_path in filtered_files:
        rel_path = file_path.relative_to(root)
        dir_path = rel_path.parent
        
        # 确保目录以 / 结尾
        dir_key = str(dir_path) + "/" if dir_path != Path(".") else "./"
        if dir_key not in dir_structure:
            dir_structure[dir_key] = []
        dir_structure[dir_key].append(rel_path.name)
    
    # 生成树结构
    for dir_key in sorted(dir_structure.keys()):
        tree_lines.append(dir_key)
        for filename in sorted(dir_structure[dir_key]):
            tree_lines.append(f"  {filename}")
    
    return "\n".join(tree_lines)

def generate_ascii_tree(files: List[Path], root: Path) -> str:
    """生成 ASCII 目录树结构 (支持无限层级)"""
    # 1. 构建嵌套的字典树结构
    # 结构示例: {'src': {'context1': {'cli.py': None, 'core': {'packer.py': None}}}}
    tree_structure = {}
    
    for file_path in files:
        try:
            rel_path = file_path.relative_to(root)
        except ValueError:
            # 如果文件不在root下，直接使用文件名
            rel_path = Path(file_path.name)
            
        parts = rel_path.parts
        current_level = tree_structure
        
        for part in parts:
            if part not in current_level:
                current_level[part] = {}
            current_level = current_level[part]

    # 2. 递归遍历树结构生成 ASCII 字符串
    tree_lines = ["# Project Structure", "."]

    def build_tree_lines(current_level: dict, prefix: str = ""):
        # 获取当前层级的所有节点（文件和文件夹），按名称排序
        entries = sorted(current_level.keys())
        
        for i, entry in enumerate(entries):
            is_last = (i == len(entries) - 1)
            
            # 确定连接符
            connector = "└── " if is_last else "├── "
            
            # 添加当前行
            tree_lines.append(f"{prefix}{connector}{entry}")
            
            # 如果该节点还有子节点（是文件夹），则递归
            # 注意：我们用空字典 {} 代表文件（叶子节点），非空字典代表文件夹
            if current_level[entry]:
                extension = "    " if is_last else "│   "
                build_tree_lines(current_level[entry], prefix + extension)

    # 开始递归
    build_tree_lines(tree_structure)
    
    return "\n".join(tree_lines)

def generate_content(files: List[Path], config: Config, tree_view: bool = True) -> str:
    """主入口：生成聚合文档内容"""
    root = config.project_root
    
    # 1. 排序
    files_sorted = sort_files(files, config)
    
    output = []
    
    # 2. 元数据提取
    architecture_map = {}
    for file_path in files_sorted:
        rel_path = file_path.relative_to(root)
        metadata = extract_metadata(file_path)
        if metadata["role"] or metadata["responsibility"]:
            architecture_map[str(rel_path)] = metadata
    
    # 3. Header & Metadata
    if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
        # Python Bundle 格式
        output.append("#!/usr/bin/env python3")
        output.append(f"# CTX1_BUNDLE_VERSION: 0.2.0")
        
        # 添加 Architecture Map
        if architecture_map:
            output.append("# ================= Architecture Map =================")
            for file_path, metadata in architecture_map.items():
                role_info = f" [{metadata['role']}]" if metadata['role'] else ""
                responsibility_info = f": {metadata['responsibility']}" if metadata['responsibility'] else ""
                output.append(f"# {file_path}{role_info}{responsibility_info}")
            output.append("# ====================================================")
        output.append("")
    else:
        # Markdown 格式
        output.append(f"# Context1 Pack Result")
        output.append(f"Generated at: {datetime.now().isoformat()}")
        output.append(f"Strategy: {config.active_strategy}")
        output.append(f"Files: {len(files_sorted)}\n")
    
    # 4. Directory Tree
    if tree_view and config.output_format_enum != OutputFormat.PYTHON_BUNDLE:
        output.append(generate_tree(files_sorted, root))
        output.append("\n")
    
    # 5. File Contents
    for file_path in files_sorted:
        rel_path = file_path.relative_to(root).as_posix()
        
        try:
            # [FIX] 内存安全检查：先看大小，再读文件
            file_stats = file_path.stat()
            file_size = file_stats.st_size
            
            if file_size > config.max_file_size_kb * 1024:
                content = f"<!-- File skipped: size ({file_size} bytes) > {config.max_file_size_kb}KB -->"
            else:
                # 尝试 UTF-8 编码，如果失败则尝试 UTF-16
                try:
                    content = file_path.read_text(encoding='utf-8')
                except UnicodeDecodeError:
                    # 如果 UTF-8 失败，尝试 UTF-16
                    try:
                        content = file_path.read_text(encoding='utf-16')
                    except UnicodeDecodeError:
                        # 如果都失败，使用二进制模式读取并转义
                        with open(file_path, 'rb') as f:
                            binary_content = f.read()
                            content = binary_content.hex()  # 转换为十六进制字符串
                        content = f"<!-- Binary file content (hex): {content} -->"
            
            if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
                # Python Bundle 格式
                output.append(f"# <ctx1:file path=\"{rel_path}\">")
                
                # 空行压缩：3行以上空行压缩为2行
                compressed_lines = []
                empty_count = 0
                for line in content.split('\n'):
                    if line.strip() == "":
                        empty_count += 1
                        if empty_count <= 2:
                            compressed_lines.append(line)
                    else:
                        empty_count = 0
                        compressed_lines.append(line)
                
                output.extend(compressed_lines)
                output.append("# </ctx1:file>")
                output.append("")
            elif config.output_format_enum == OutputFormat.MARKDOWN:
                # Markdown 格式
                output.append(f"--- 文件: {rel_path} ---")
                output.append(content)
                output.append("\n")
            else:
                # XML 格式（保留原有逻辑）
                output.append(f'<document path="{rel_path}">')
                output.append(content)
                output.append('</document>\n')
                
        except Exception as e:
            if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
                output.append(f"# <!-- Error reading {rel_path}: {str(e)} -->")
            else:
                output.append(f"<!-- Error reading {rel_path}: {str(e)} -->\n")
    
    # 6. 生成布局蓝图
    # 6. 生成布局蓝图 (已移至CLI层，避免重复生成)
    
    # 7. 封装输出
    if config.output_format_enum == OutputFormat.PYTHON_BUNDLE:
        return "\n".join(output)
    elif config.output_format_enum == OutputFormat.MARKDOWN:
        return "\n".join(output)
    else:
        return "<documents>\n" + "\n".join(output) + "\n</documents>"

