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
            
            # 如果文件为空，则不是二进制文件
            if not chunk:
                return False
            
            # 检查是否包含 NULL 字节
            has_null = b'\x00' in chunk
            
            # 如果包含 NULL 字节，检查是否可能是 UTF-16 编码的文本
            if has_null:
                # 检查是否是 UTF-16 BOM
                if chunk.startswith(b'\xff\xfe') or chunk.startswith(b'\xfe\xff'):
                    # 可能是 UTF-16 编码的文本，不是二进制文件
                    return False
                
                # 检查是否是纯文本的 UTF-16 编码（每个字符后跟 NULL 字节）
                # 如果大部分字符都是字母数字，并且 NULL 字节规律分布，可能是 UTF-16 文本
                null_positions = [i for i, b in enumerate(chunk) if b == 0]
                if len(null_positions) > 0:
                    # 检查 NULL 字节是否规律分布（每2个字节一个NULL）
                    is_utf16_pattern = True
                    for i in range(1, len(null_positions)):
                        if null_positions[i] - null_positions[i-1] != 2:
                            is_utf16_pattern = False
                            break
                    
                    # 如果大部分内容都是可打印字符，可能是 UTF-16 文本
                    printable_count = sum(1 for b in chunk if 32 <= b <= 126)
                    if is_utf16_pattern and printable_count > len(chunk) * 0.3:
                        return False
            
            # 如果包含 NULL 字节且不是 UTF-16 文本，则是二进制文件
            if has_null:
                return True
            
            # 如果没有 NULL 字节，则不是二进制文件
            return False
            
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