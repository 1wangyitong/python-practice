import pytest
import allure
import jsonschema
from faker import Faker  # 1. 加上这两行！必须在最上面导入

fake = Faker('zh_CN')

@allure.feature("用户鉴权模块")
def test_auth_token_flow(api_client, auth_token):
    """这是你之前写好的基础鉴权测试"""
    allure.dynamic.story("携带 Token 获取用户信息")
    print(f"\n拿到测试用的 Token :{auth_token}")
    
    assert auth_token is not None
    response_data = api_client.get_user_info(auth_token)
    received_headers = response_data["headers"]
    
    with allure.step("断言 Token 是否正确发送"):
        assert "Authorization" in received_headers
        assert received_headers["Authorization"] == f"Bearer {auth_token}"

@allure.feature("用户鉴权模块")
# 换成 fake.user_name()，它会生成类似 'john_doe' 这样的随机英文名
@pytest.mark.parametrize("test_user", [fake.user_name(), fake.user_name()])
def test_auth_token_flow_with_faker(api_client, test_user):
    """这是你今天新写的 Faker 随机用户测试"""
    allure.dynamic.story("使用随机生成的假用户进行登录测试")
    
    # 使用 faker 生成的假名字去登录
    token = api_client.login(test_user, "password123")
    print(f"\n随机用户 {test_user} 登录成功，获取到 Token: {token}")
    
    # 断言 1：Token 不为空
    assert token is not None
    
    # 带着 Token 去请求
    response_data = api_client.get_user_info(token)
    
    # 断言 2：检查请求头
    assert "Authorization" in response_data["headers"]
    
    # 断言 3：Schema 结构校验
    with allure.step("校验接口返回的 JSON Schema 结构"):
        expected_schema = {
            "type": "object",
            "required": ["headers"]
        }
        jsonschema.validate(instance=response_data, schema=expected_schema)