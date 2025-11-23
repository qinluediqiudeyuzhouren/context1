"""
src/context1/core/unpacker.py
还原器 - 核心职责：解析聚合文档、提取文件、安全写入
[修正版] 修复了 Python 缩进错误，优化了 strip 逻辑以保护数据完整性
"""
import re
from pathlib import Path
from typing import List, Dict, Tuple
from context1.utils.fs import safe_write_file

MD_PATTERN = re.compile(r'^--- 文件: (.+?) ---$')
XML_PATTERN = re.compile(r'<document path="(.+?)">')

def parse_document(content: str) -> List[Dict[str, str]]:
    """
    解析文档内容，返回文件列表
    """
    lines = content.split('\n')
    files = []
    
    current_file = None
    current_content = []
    
    for line in lines:
        # Markdown Header Match
        md_match = MD_PATTERN.match(line)
        if md_match:
            if current_file:
                files.append({
                    'path': current_file,
                    # [FIX] 不移除行首缩进，仅移除尾部多余换行
                    'content': '\n'.join(current_content) 
                })
            current_file = md_match.group(1).strip()
            current_content = []
            continue
            
        # XML Header Match
        xml_match = XML_PATTERN.match(line)
        if xml_match:
            # [FIX] 缩进已修复，与上一层 if 对齐
            if current_file:
                files.append({
                    'path': current_file,
                    'content': '\n'.join(current_content)
                })
            current_file = xml_match.group(1).strip()
            current_content = []
            continue
             
        # Content Collection
        if current_file:
            if line.strip() == '</document>':
                continue
            current_content.append(line)
            
    # Save last file
    if current_file:
        files.append({
            'path': current_file,
            'content': '\n'.join(current_content)
        })
        
    return files

def unpack_project(
    source_file: Path, 
    output_dir: Path, 
    force: bool = False,
    structure_only: bool = False
) -> Dict[str, int]:
    """
    执行还原操作
    """
    if not source_file.exists():
        raise FileNotFoundError(f"Source file not found: {source_file}")
        
    content = source_file.read_text(encoding='utf-8')
    files = parse_document(content)
    
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