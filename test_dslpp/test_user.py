# 测试文件
@Role: Test
@Responsibility: 用户模块测试
import unittest

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = {"name": "Test", "email": "test@example.com"}
        self.assertEqual(user["name"], "Test")