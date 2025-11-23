"""
测试文件系统安全性 - 核心职责：测试路径安全检查、Zip Slip 防护
"""
import pytest
import tempfile
import os
from pathlib import Path
import sys

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from context1.utils.fs import is_safe_path

def test_is_safe_path_basic():
    """测试基本的安全路径检查"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 同一目录下的文件应该是安全的
        assert is_safe_path(base, "file.txt") == True
        assert is_safe_path(base, "subdir/file.txt") == True
        
        # 父目录应该是安全的
        assert is_safe_path(base, "..") == False
        assert is_safe_path(base, "../other") == False

def test_is_safe_path_absolute():
    """测试绝对路径的安全性"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 绝对路径指向同一目录应该是安全的
        abs_path = base / "file.txt"
        assert is_safe_path(base, str(abs_path)) == True
        
        # 绝对路径指向子目录应该是安全的
        subdir = base / "subdir"
        subdir.mkdir()
        abs_subdir_path = subdir / "file.txt"
        assert is_safe_path(base, str(abs_subdir_path)) == True
        
        # 绝对路径指向完全不同的目录应该是危险的
        with tempfile.TemporaryDirectory() as other_temp_dir:
            other_base = Path(other_temp_dir)
            other_abs_path = other_base / "file.txt"
            assert is_safe_path(base, str(other_abs_path)) == False

def test_is_safe_path_zip_slip_attack():
    """测试 Zip Slip 攻击防护"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 测试 Zip Slip 攻击模式
        attack_paths = [
            "../../../etc/passwd",
            "..\\..\\..\\windows\\system32\\config\\sam",
            "subdir/../../../etc/passwd",
            "subdir/..\\..\\..\\windows\\system32\\config\\sam",
        ]
        
        for attack_path in attack_paths:
            assert is_safe_path(base, attack_path) == False, f"Path '{attack_path}' should be blocked"

def test_is_safe_path_edge_cases():
    """测试边界情况"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 空路径
        assert is_safe_path(base, "") == True
        
        # 点路径
        assert is_safe_path(base, ".") == True
        
        # 相对路径到自身
        assert is_safe_path(base, "./file.txt") == True
        
        # 多层相对路径
        assert is_safe_path(base, "a/b/c/file.txt") == True

def test_is_safe_path_with_symlinks():
    """测试符号链接处理（如果支持）"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base = Path(temp_dir)
        
        # 创建一个符号链接指向外部目录
        try:
            external_file = Path(temp_dir) / "external.txt"
            external_file.write_text("test")
            
            symlink_path = base / "symlink"
            symlink_path.symlink_to(external_file)
            
            # 符号链接指向外部文件应该是安全的（如果解析后仍在 base 内）
            assert is_safe_path(base, "symlink") == True
            
        except (OSError, NotImplementedError):
            # 如果不支持符号链接，跳过测试
            pytest.skip("Symbolic links not supported on this platform")

if __name__ == "__main__":
    pytest.main([__file__])