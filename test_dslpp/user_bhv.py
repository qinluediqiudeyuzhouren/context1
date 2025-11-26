# 行为层
@Role: Behavior
@Responsibility: 用户行为逻辑
class UserBehavior:
    def validate_email(self, email):
        return "@" in email and "." in email