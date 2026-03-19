# config/config_loader.py
from dotenv import load_dotenv
import os
import sys

def load_env():
    """
    加载 config 目录下的 .env 文件
    返回值：加载成功返回 True，失败返回 False
    """
    # 1. 获取当前脚本（config_loader.py）的绝对路径
    current_file = os.path.abspath(__file__)
    # 2. 获取 config 目录的路径（当前脚本所在目录）
    config_dir = os.path.dirname(current_file)
    # 3. 拼接 .env 文件的完整路径
    env_path = os.path.join(config_dir, ".env")
    
    # 4. 检查 .env 文件是否存在（可选，但更友好）
    if not os.path.exists(env_path):
        print(f"❌ 错误：未找到 .env 文件，路径：{env_path}", file=sys.stderr)
        return False
    
    # 5. 加载 .env 文件
    load_dotenv(env_path)
    print(f"✅ 成功加载 .env 文件，路径：{env_path}")
    return True

def get_env_var(key, default=None):
    """
    读取环境变量（封装 os.getenv，更便捷）
    :param key: 环境变量名
    :param default: 可选，默认值（变量不存在时返回）
    :return: 环境变量值
    """
    value = os.getenv(key, default)
    if value is None and default is None:
        print(f"⚠️ 警告：环境变量 {key} 未配置", file=sys.stderr)
    return value

# 测试代码（可选，直接运行该脚本时验证）
# if __name__ == "__main__":
#     load_env()
#     # 测试读取配置
#     db_pwd = get_env_var("DB_PASSWORD")
#     print(f"测试读取配置：DB_PASSWORD = {db_pwd}")