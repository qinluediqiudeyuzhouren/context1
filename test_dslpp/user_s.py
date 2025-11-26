# 服务层
@Role: Service
@Responsibility: 用户服务实现
from .user_i import UserServiceInterface

class UserService(UserServiceInterface):
    def create_user(self, name, email):
        return f"User {name} created successfully"