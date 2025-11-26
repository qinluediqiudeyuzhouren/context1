# 策略层
@Role: Strategy
@Responsibility: 用户策略定义
class UserStrategy:
    def process_user(self, user_data):
        return f"Processing user: {user_data['name']}"