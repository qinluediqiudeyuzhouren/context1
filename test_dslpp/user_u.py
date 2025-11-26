# 工具层
@Role: Utility
@Responsibility: 用户相关工具函数
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()