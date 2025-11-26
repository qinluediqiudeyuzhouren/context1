# 控制器层
@Role: Controller
@Responsibility: 用户控制器逻辑
from .user_i import UserServiceInterface

class UserController(UserServiceInterface):
    def create_user(self, name, email):
        return f"User {name} created with email {email}"