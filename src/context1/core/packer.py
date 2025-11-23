"""
src/context1/core/packer.py
打包器 - 核心职责：生成目录树、文件排序、格式化输出(Markdown/XML)
[修正版] 增加了内存溢出保护 (Pre-read size check)
"""
from pathlib import Path
from typing import List
from datetime import datetime
from context1.core.config import Config

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

def generate_tree(files: List[Path], root: Path) -> str:
    """生成 ASCII 目录树结构 (类似 Linux tree 命令)"""
    tree_lines = ["# Project Structure"]
    tree_lines.append(".")
    
    # 按目录分组文件
    dir_files = {}
    for file_path in files:
        rel_path = file_path.relative_to(root)
        dir_path = rel_path.parent
        if dir_path not in dir_files:
            dir_files[dir_path] = []
        dir_files[dir_path].append(rel_path)
    
    # 生成目录树
    def build_tree_display(path: Path, prefix: str = "", is_last: bool = True) -> List[str]:
        lines = []
        name = path.name if path != Path(".") else "."
        lines.append(f"{prefix}{'└── ' if is_last else '├── '}{name}")
        
        if path in dir_files:
            children = sorted(dir_files[path], key=lambda x: (x.is_file(), x.name))
            for i, child in enumerate(children):
                child_prefix = prefix + ("    " if is_last else "│   ")
                is_last_child = i == len(children) - 1
                if child.is_file():
                    lines.append(f"{child_prefix}{'└── ' if is_last_child else '├── '}{child.name}")
                else:
                    lines.extend(build_tree_display(child, child_prefix, is_last_child))
        
        return lines
    
    # 从根目录开始构建
    root_files = [f for f in files if f.parent == root]
    root_dirs = [d for d in dir_files.keys() if d != Path(".") and d.parent == root]
    
    # 先显示根目录文件
    for i, file_path in enumerate(sorted(root_files, key=lambda x: x.name)):
        is_last = i == len(root_files) - 1 and len(root_dirs) == 0
        prefix = "" if is_last else "│   "
        lines = build_tree_display(file_path.relative_to(root), prefix, is_last)
        tree_lines.extend(lines)
    
    # 再显示根目录
    for i, dir_path in enumerate(sorted(root_dirs, key=lambda x: x.name)):
        is_last = i == len(root_dirs) - 1
        prefix = "" if is_last else "│   "
        lines = build_tree_display(dir_path, prefix, is_last)
        tree_lines.extend(lines)
    
    return "\n".join(tree_lines)

def generate_content(files: List[Path], config: Config, tree_view: bool = True) -> str:
    """主入口：生成聚合文档内容"""
    root = config.project_root
    
    # 1. 排序
    files_sorted = sorted(files, key=lambda f: vscode_sort_key(f.relative_to(root)))
    
    output = []
    
    # 2. Header & Metadata
    output.append(f"# Context1 Pack Result")
    output.append(f"Generated at: {datetime.now().isoformat()}")
    output.append(f"Strategy: {config.active_strategy}")
    output.append(f"Files: {len(files_sorted)}\n")
    
    # 3. Directory Tree
    if tree_view:
        output.append(generate_tree(files_sorted, root))
        output.append("\n")
        
    # 4. File Contents
    for file_path in files_sorted:
        rel_path = file_path.relative_to(root).as_posix()
        
        try:
            # [FIX] 内存安全检查：先看大小，再读文件
            file_stats = file_path.stat()
            file_size = file_stats.st_size
            
            if file_size > config.max_file_size_kb * 1024:
                content = f"<!-- File skipped: size ({file_size} bytes) > {config.max_file_size_kb}KB -->"
            else:
                content = file_path.read_text(encoding='utf-8', errors='replace')
            
            if config.output_format == "xml":
                # XML Format
                output.append(f'<document path="{rel_path}">')
                output.append(content)
                output.append('</document>\n')
            else:
                # Markdown Format
                output.append(f"--- 文件: {rel_path} ---")
                output.append(content)
                output.append("\n")
                
        except Exception as e:
            output.append(f"<!-- Error reading {rel_path}: {str(e)} -->\n")
            
    if config.output_format == "xml":
        return "<documents>\n" + "\n".join(output) + "\n</documents>"
        
    return "\n".join(output)