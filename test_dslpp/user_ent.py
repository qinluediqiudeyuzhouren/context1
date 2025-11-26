# 实体类文件
@Role: Entity
@Responsibility: 用户数据实体定义
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email