# 命令层
@Role: Commander
@Responsibility: 用户命令处理
class UserCommand:
    def execute(self, user_data):
        return f"Command executed for user: {user_data['name']}"