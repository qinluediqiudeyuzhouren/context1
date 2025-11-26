# 接口层
@Role: Interface
@Responsibility: 用户服务接口定义
from abc import ABC, abstractmethod

class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, name, email):
        pass