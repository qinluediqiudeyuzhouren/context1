# 数据访问层
@Role: Data
@Responsibility: 用户数据访问逻辑
class UserData:
    def get_user(self, user_id):
        return {"id": user_id, "name": "Test User"}