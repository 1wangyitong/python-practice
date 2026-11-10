# 新建全局配置文件
import pytest

# 定义一个全局的 fixture（夹具）
@pytest.fixture(scope="session") # scope="session" 代表整个测试过程只执行一次
def base_url():
    return "https://jsonplaceholder.typicode.com"