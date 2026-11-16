# 新建全局配置文件
import pytest

# # 定义一个全局的 fixture（夹具）
# @pytest.fixture(scope="session") # scope="session" 代表整个测试过程只执行一次
# def base_url():
#     return "https://jsonplaceholder.typicode.com"

from api.api_client import WeatherAPI

# 这个 fixture 用来提供 WeatherAPI 实例
@pytest.fixture(scope = "session")
def weather_api():
    return WeatherAPI()