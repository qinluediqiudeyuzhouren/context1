"""
单元测试 - Packer 模块
测试 DS-LPP 排序、Python Bundle 格式生成、元数据提取等功能
"""
import pytest
import tempfile
from pathlib import Path
from context1.core.config import Config, OutputFormat, SortStrategy, DEFAULT_DSLPP_WEIGHTS
from context1.core.packer import (
    calculate_dslpp_weight, 
    sort_files, 
    extract_metadata, 
    generate_layout_tree,
    generate_content
)


class TestDSLPPSorting:
    """测试 DS-LPP 排序功能"""
    
    def test_calculate_dslpp_weight_init(self):
        """测试 __init__.py 权重"""
        weight = calculate_dslpp_weight("__init__.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 0
    
    def test_calculate_dslpp_weight_entity(self):
        """测试实体文件权重"""
        weight = calculate_dslpp_weight("user_entity.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 10
    
    def test_calculate_dslpp_weight_command(self):
        """测试命令文件权重"""
        weight = calculate_dslpp_weight("search_cmd.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 40
    
    def test_calculate_dslpp_weight_test(self):
        """测试文件权重"""
        weight = calculate_dslpp_weight("test_user_service.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 99
    
    def test_calculate_dslpp_weight_default(self):
        """测试默认权重"""
        weight = calculate_dslpp_weight("unknown_file.py", DEFAULT_DSLPP_WEIGHTS)
        assert weight == 50
    
    def test_sort_files_dslpp(self):
        """测试 DS-LPP 排序"""
        files = [
            Path("test_user_service.py"),
            Path("__init__.py"),
            Path("user_entity.py"),
            Path("search_cmd.py"),
            Path("user_service.py")
        ]
        
        config = Config(
            project_root=Path("/test"),
            sort_strategy=SortStrategy.DSLPP,
            dslpp_weights=DEFAULT_DSLPP_WEIGHTS
        )
        
        sorted_files = sort_files(files, config)
        
        # 验证排序结果
        assert str(sorted_files[0]) == "__init__.py"
        assert str(sorted_files[1]) == "user_entity.py"
        assert str(sorted_files[2]) == "user_service.py"
        assert str(sorted_files[3]) == "search_cmd.py"
        assert str(sorted_files[4]) == "test_user_service.py"


class TestMetadataExtraction:
    """测试元数据提取功能"""
    
    def test_extract_metadata_with_role(self):
        """测试提取角色信息"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("""
# @Role: Commander
# @Responsibility: 搜索入口
def search():
    pass
""")
            temp_file = Path(f.name)
        
        try:
            metadata = extract_metadata(temp_file)
            assert metadata["role"] == "Commander"
            assert metadata["responsibility"] == "搜索入口"
        finally:
            temp_file.unlink()
    
    def test_extract_metadata_without_role(self):
        """测试无角色信息的文件"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write("""
def simple_function():
    pass
""")
            temp_file = Path(f.name)
        
        try:
            metadata = extract_metadata(temp_file)
            assert metadata["role"] == ""
            assert metadata["responsibility"] == ""
        finally:
            temp_file.unlink()


class TestPythonBundle:
    """测试 Python Bundle 格式生成"""
    
    def test_generate_content_python_bundle(self):
        """测试 Python Bundle 格式生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            test_file = temp_path / "test.py"
            test_file.write_text('print("Hello, World!")\n')
            
            files = [test_file]
            config = Config(
                project_root=temp_path,
                output_format_enum=OutputFormat.PYTHON_BUNDLE,
                sort_strategy=SortStrategy.NAME
            )
            
            content = generate_content(files, config, tree_view=False)
            
            # 验证 Python Bundle 格式
            assert "#!/usr/bin/env python3" in content
            assert "# CTX1_BUNDLE_VERSION: 0.2.0" in content
            assert '# <ctx1:file path="test.py">' in content
            assert "# </ctx1:file>" in content
            assert 'print("Hello, World!")' in content
    
    def test_generate_content_markdown(self):
        """测试 Markdown 格式生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            test_file = temp_path / "test.py"
            test_file.write_text('print("Hello, World!")\n')
            
            files = [test_file]
            config = Config(
                project_root=temp_path,
                output_format_enum=OutputFormat.MARKDOWN,
                sort_strategy=SortStrategy.NAME
            )
            
            content = generate_content(files, config, tree_view=False)
            
            # 验证 Markdown 格式
            assert "--- 文件: test.py ---" in content
            assert 'print("Hello, World!")' in content


class TestLayoutTree:
    """测试布局蓝图生成"""
    
    def test_generate_layout_tree(self):
        """测试布局蓝图生成"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试文件
            (temp_path / "src").mkdir()
            (temp_path / "tests").mkdir()
            
            (temp_path / "src" / "main.py").write_text("def main(): pass")
            (temp_path / "src" / "utils.py").write_text("def util(): pass")
            (temp_path / "tests" / "test_main.py").write_text("def test_main(): pass")
            (temp_path / "README.md").write_text("# Test Project")
            
            files = [
                temp_path / "src" / "main.py",
                temp_path / "src" / "utils.py",
                temp_path / "tests" / "test_main.py",
                temp_path / "README.md"
            ]
            
            tree_content = generate_layout_tree(files, temp_path)
            
            # 验证树格式
            assert "src/" in tree_content
            assert "tests/" in tree_content
            assert "main.py" in tree_content
            assert "utils.py" in tree_content
            assert "test_main.py" in tree_content
            assert "README.md" in tree_content


if __name__ == "__main__":
    pytest.main([__file__])