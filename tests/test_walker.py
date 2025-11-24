"""
测试文件扫描器 - 核心职责：测试文件过滤、Gitignore集成、策略过滤
"""
import pytest
import tempfile
import json
import os
from pathlib import Path
import sys

# 添加 src 到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from context1.core.config import Config
from context1.core.walker import FileWalker

def create_test_files(base_dir: Path):
    """创建测试文件结构"""
    # 创建各种类型的文件
    (base_dir / "main.py").write_text("# Main file")
    (base_dir / "test.py").write_text("# Test file")
    (base_dir / "data.json").write_text('{"key": "value"}')
    (base_dir / "README.md").write_text("# README")
    (base_dir / "config.toml").write_text("[tool.poetry]\nname = 'test'")
    
    # 创建二进制文件
    (base_dir / "binary.exe").write_bytes(b"\x00\x01\x02\x03")
    (base_dir / "image.png").write_bytes(b"\x89PNG\r\n\x1a\n")
    
    # 创建锁定文件
    (base_dir / "package-lock.json").write_text("{}")
    (base_dir / "yarn.lock").write_text("# yarn lock")
    (base_dir / "poetry.lock").write_text("# poetry lock")
    
    # 创建子目录
    subdir = base_dir / "src"
    subdir.mkdir()
    (subdir / "module.py").write_text("# Module file")
    (subdir / "test.lock").write_text("# Test lock file")
    
    # 创建 .gitignore
    (base_dir / ".gitignore").write_text("""
__pycache__/
*.pyc
*.pyo
*.pyd
*.class
*.lock
.venv/
venv/
env/
node_modules/
""")

def test_walker_excludes_lock_files():
    """测试 walker 是否正确排除 .lock 文件"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            always_exclude=["*.lock"]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否有 .lock 文件
        lock_files = [f for f in files if f.name.endswith('.lock')]
        assert len(lock_files) == 0, f"Found lock files that should be excluded: {lock_files}"

def test_walker_excludes_binary_files():
    """测试 walker 是否正确排除二进制文件"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            binary_extensions=[".exe", ".png"]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否有二进制文件
        binary_files = [f for f in files if f.suffix.lower() in ['.exe', '.png']]
        assert len(binary_files) == 0, f"Found binary files that should be excluded: {binary_files}"

def test_walker_respects_gitignore():
    """测试 walker 是否正确遵循 .gitignore"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            use_gitignore=True,
            always_exclude=[]
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 检查是否排除了 .gitignore 中指定的文件
        file_names = [f.name for f in files]
        
        # 应该排除的文件
        excluded_patterns = ["__pycache__", "*.pyc", "*.pyo", "*.pyd", "*.lock", ".venv", "venv", "env", "node_modules"]
        
        # 检查是否有被排除的文件
        for pattern in excluded_patterns:
            if pattern.endswith('*'):
                # 处理通配符
                prefix = pattern[:-1]
                matching_files = [f for f in file_names if f.startswith(prefix)]
                assert len(matching_files) == 0, f"Found files matching pattern '{pattern}': {matching_files}"
            else:
                assert pattern not in file_names, f"Found excluded file: {pattern}"

def test_walker_smart_strategy():
    """测试 smart 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="smart"
        )
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该找到所有非二进制、非锁定、非排除的文件
        expected_files = ["main.py", "test.py", "data.json", "README.md", "config.toml"]
        file_names = [f.name for f in files]
        
        for expected_file in expected_files:
            assert expected_file in file_names, f"Expected file '{expected_file}' not found in scan results"

def test_walker_blacklist_strategy():
    """测试 blacklist 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="blacklist"
        )
        
        # 创建黑名单策略文件
        ctx_dir = base_dir / ".context1"
        ctx_dir.mkdir()

        blacklist_file = ctx_dir / "blacklist.json"
        blacklist_data = {
            "patterns": ["*.json", "src/"]
        }
        with open(blacklist_file, 'w') as f:
            json.dump(blacklist_data, f)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该排除 .json 文件和 src 目录
        file_names = [f.name for f in files]
        relative_paths = [str(f.relative_to(base_dir)) for f in files]
        
        # 检查是否排除了 .json 文件
        json_files = [f for f in file_names if f.endswith('.json')]
        assert len(json_files) == 0, f"Found JSON files that should be blacklisted: {json_files}"
        
        # 检查是否排除了 src 目录
        src_files = [f for f in relative_paths if f.startswith('src/')]
        assert len(src_files) == 0, f"Found src directory files that should be blacklisted: {src_files}"

def test_walker_whitelist_strategy():
    """测试 whitelist 策略下的文件扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        create_test_files(base_dir)
        
        # 创建配置
        config = Config(
            project_root=base_dir,
            active_strategy="whitelist"
        )
        
        # 创建白名单策略文件
        ctx_dir = base_dir / ".context1"
        ctx_dir.mkdir()

        whitelist_file = ctx_dir / "whitelist.json"
        whitelist_data = {
            "patterns": ["*.py", "README.md"]
        }
        with open(whitelist_file, 'w') as f:
            json.dump(whitelist_data, f)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该只包含 .py 文件和 README.md
        file_names = [f.name for f in files]
        
        # 检查是否只包含白名单文件
        for file_name in file_names:
            assert file_name.endswith('.py') or file_name == 'README.md', f"Found non-whitelisted file: {file_name}"

def test_walker_empty_directory():
    """测试空目录的扫描"""
    with tempfile.TemporaryDirectory() as temp_dir:
        base_dir = Path(temp_dir)
        
        # 创建配置
        config = Config(project_root=base_dir)
        
        # 扫描文件
        walker = FileWalker(config)
        files = walker.scan()
        
        # 应该返回空列表
        assert len(files) == 0, f"Expected no files in empty directory, found: {files}"

if __name__ == "__main__":
    pytest.main([__file__])