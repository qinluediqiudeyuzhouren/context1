"""
单元测试 - Unpacker 模块
测试文档解析、智能内容池、结构树驱动注入等功能
"""
import pytest
import tempfile
from pathlib import Path
from context1.core.unpacker import (
    parse_document,
    ContentPool,
    parse_layout_tree,
    calculate_path_similarity,
    resolve_target,
    unpack_project
)


class TestDocumentParsing:
    """测试文档解析功能"""
    
    def test_parse_markdown_format(self):
        """测试 Markdown 格式解析"""
        content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")

--- 文件: src/utils.py ---
def util():
    pass"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'
    
    def test_parse_xml_format(self):
        """测试 XML 格式解析"""
        content = """<document path="src/main.py">
def main():
    print("Hello, World!")
</document>

<document path="src/utils.py">
def util():
    pass
</document>"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'
    
    def test_parse_python_bundle_format(self):
        """测试 Python Bundle 格式解析"""
        content = """#!/usr/bin/env python3
# CTX1_BUNDLE_VERSION: 0.2.0

# <ctx1:file path="src/main.py">
def main():
    print("Hello, World!")
# </ctx1:file>

# <ctx1:file path="src/utils.py">
def util():
    pass
# </ctx1:file>"""
        
        files = parse_document(content)
        
        assert len(files) == 2
        assert files[0]['path'] == "src/main.py"
        assert files[0]['content'] == 'def main():\n    print("Hello, World!")'
        assert files[1]['path'] == "src/utils.py"
        assert files[1]['content'] == 'def util():\n    pass'


class TestContentPool:
    """测试智能内容池功能"""
    
    def test_content_pool_creation(self):
        """测试内容池创建"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'src/utils.py', 'content': 'def util(): pass'},
            {'path': 'tests/test_main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        assert len(pool.pool) == 3
        assert 'main.py' in pool.pool
        assert 'utils.py' in pool.pool
        assert 'test_main.py' in pool.pool
    
    def test_content_pool_unique_match(self):
        """测试唯一匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        result = pool.get_file('main.py')
        
        assert result is not None
        assert result[0] == 'src/main.py'
        assert result[1] == 'def main(): pass'
    
    def test_content_pool_multiple_files(self):
        """测试多文件同名情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试获取所有同名文件
        all_files = pool.get_all_files('main.py')
        assert len(all_files) == 2
        assert all_files[0][0] == 'src/main.py'
        assert all_files[1][0] == 'tests/main.py'
        
        # 测试唯一匹配（应该返回 None）
        unique = pool.get_file('main.py')
        assert unique is None


class TestLayoutTree:
    """测试布局树功能"""
    
    def test_parse_layout_tree(self):
        """测试布局树解析"""
        tree_content = """# Project Structure
src/
    main.py
    utils.py
tests/
    test_main.py
    test_utils.py
README.md
"""
        
        target_paths = parse_layout_tree(tree_content)
        
        assert len(target_paths) == 5
        assert 'src/main.py' in target_paths
        assert 'src/utils.py' in target_paths
        assert 'tests/test_main.py' in target_paths
        assert 'tests/test_utils.py' in target_paths
        assert 'README.md' in target_paths
    
    def test_parse_layout_tree_with_directories(self):
        """测试包含目录的布局树解析"""
        tree_content = """# Project Structure
src/
    main.py
    utils/
        helper.py
tests/
    test_main.py
"""
        
        target_paths = parse_layout_tree(tree_content)
        
        assert len(target_paths) == 3
        assert 'src/main.py' in target_paths
        assert 'src/utils/helper.py' in target_paths
        assert 'tests/test_main.py' in target_paths


class TestPathSimilarity:
    """测试路径相似度计算"""
    
    def test_path_similarity_same_path(self):
        """测试相同路径"""
        similarity = calculate_path_similarity('src/main.py', 'src/main.py')
        assert similarity == 2  # 'src' + 'main.py'
    
    def test_path_similarity_common_prefix(self):
        """测试公共前缀"""
        similarity = calculate_path_similarity('src/main.py', 'src/utils.py')
        assert similarity == 1  # 'src'
    
    def test_path_similarity_different_prefix(self):
        """测试不同前缀"""
        similarity = calculate_path_similarity('src/main.py', 'tests/main.py')
        assert similarity == 0  # 无公共部分
    
    def test_path_similarity_nested(self):
        """测试嵌套路径"""
        similarity = calculate_path_similarity('src/utils/helper.py', 'src/utils/main.py')
        assert similarity == 2  # 'src' + 'utils'


class TestTargetResolution:
    """测试目标路径解析"""
    
    def test_resolve_target_unique_match(self):
        """测试唯一匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        status, content = resolve_target('src/main.py', pool)
        
        assert status == 'match'
        assert content == ('src/main.py', 'def main(): pass')
    
    def test_resolve_target_path_similarity(self):
        """测试路径相似度匹配"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试匹配 src/main.py
        status, content = resolve_target('src/main.py', pool)
        assert status == 'match'
        assert content[0] == 'src/main.py'
        
        # 测试匹配 tests/main.py
        status, content = resolve_target('tests/main.py', pool)
        assert status == 'match'
        assert content[0] == 'tests/main.py'
    
    def test_resolve_target_conflict(self):
        """测试冲突情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'},
            {'path': 'tests/main.py', 'content': 'def test_main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试冲突（两个路径相似度相同）
        status, content = resolve_target('other/main.py', pool)
        assert status == 'conflict'
        assert 'Conflict resolution' in content
    
    def test_resolve_target_scaffold(self):
        """测试脚手架情况"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试不存在的文件
        status, content = resolve_target('src/new_file.py', pool)
        assert status == 'scaffold'
        assert 'Generated by Context1 scaffold' in content
    
    def test_resolve_target_init_special_case(self):
        """测试 __init__.py 特殊处理"""
        files = [
            {'path': 'src/main.py', 'content': 'def main(): pass'}
        ]
        
        pool = ContentPool(files)
        
        # 测试 __init__.py 特殊处理
        status, content = resolve_target('src/__init__.py', pool)
        assert status == 'scaffold'
        assert 'Generated by Context1 scaffold' in content


class TestUnpackProject:
    """测试解包项目功能"""
    
    def test_unpack_project_normal_mode(self):
        """测试普通模式解包"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试 bundle
            bundle_content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")

--- 文件: src/utils.py ---
def util():
    pass"""
            
            bundle_file = temp_path / "test.ctx1.md"
            bundle_file.write_text(bundle_content)
            
            # 解包到新目录
            output_dir = temp_path / "output"
            stats = unpack_project(bundle_file, output_dir)
            
            # 验证结果
            assert stats['success'] == 2
            assert stats['skipped'] == 0
            assert stats['failed'] == 0
            
            # 验证文件是否正确创建
            assert (output_dir / "src" / "main.py").exists()
            assert (output_dir / "src" / "utils.py").exists()
    
    def test_unpack_project_dry_run(self):
        """测试试运行模式"""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            
            # 创建测试 bundle
            bundle_content = """--- 文件: src/main.py ---
def main():
    print("Hello, World!")"""
            
            bundle_file = temp_path / "test.ctx1.md"
            bundle_file.write_text(bundle_content)
            
            # 创建结构树
            tree_content = """src/
    main.py
    new_file.py"""
            
            tree_file = temp_path / "layout.tree"
            tree_file.write_text(tree_content)
            
            # 试运行
            output_dir = temp_path / "output"
            stats = unpack_project(
                bundle_file, 
                output_dir, 
                tree_path=tree_file,
                dry_run=True
            )
            
            # 验证结果
            assert stats['match'] == 1  # main.py 匹配
            assert stats['scaffold'] == 1  # new_file.py 脚手架
            assert stats['conflict'] == 0
            assert stats['failed'] == 0
            
            # 验证文件未实际创建
            assert not output_dir.exists()


if __name__ == "__main__":
    pytest.main([__file__])