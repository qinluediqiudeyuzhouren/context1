"""
src/context1/utils/fs.py
文件系统操作工具集 - 核心职责：路径安全检查、二进制检测、文件读写封装
[修正版] 已修复 Zip Slip 漏洞，使用 os.path.commonpath
"""
import os
from pathlib import Path
from typing import Union

def is_safe_path(base_dir: Union[str, Path], target_path: Union[str, Path]) -> bool:
    """
    【核心安全逻辑】Zip Slip 防护
    使用 pathlib 的相对_to() 方法确保 target 在 base 目录下
    """
    try:
        base = Path(base_dir).resolve()
        
        # 允许 target_path 是绝对路径或相对路径
        if os.path.isabs(target_path):
            target = Path(target_path).resolve()
        else:
            target = (base / target_path).resolve()
            
        # 使用 pathlib 的相对_to() 方法进行安全检查
        # 如果 target 不在 base 目录下，会抛出 ValueError
        try:
            relative = target.relative_to(base)
            # 检查相对路径是否包含向上导航的组件
            return not any(part == '..' for part in relative.parts)
        except ValueError:
            # target 不在 base 目录下
            return False
            
    except Exception:
        return False

def is_binary_file(file_path: Path, chunk_size: int = 1024) -> bool:
    """
    通过读取前 chunk_size 字节检查是否包含 NULL 字节来判断是否为二进制文件
    """
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(chunk_size)
            return b'\x00' in chunk
    except IOError:
        return False

def get_project_root(start_path: Path = Path(".")) -> Path:
    """
    向上递归查找包含 .context1/ 的目录，如果找不到则返回 start_path
    """
    current = start_path.resolve()
    for parent in [current, *current.parents]:
        if (parent / ".context1").is_dir():
            return parent
    return current

def safe_write_file(base_dir: Path, rel_path: str, content: str, force: bool = False) -> bool:
    """
    安全写入文件
    """
    if not is_safe_path(base_dir, rel_path):
        raise ValueError(f"Unsafe path detected: {rel_path}")
    
    target_file = (base_dir / rel_path).resolve()
    
    # 检查文件是否存在
    if target_file.exists() and not force:
        return False
    
    # 自动创建父目录
    target_file.parent.mkdir(parents=True, exist_ok=True)
    
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return True