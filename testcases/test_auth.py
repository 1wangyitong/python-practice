import pytest
import allure
import jsonschema

@allure.feature("用户鉴权模块")
def test_auth_token_flow(api_client, auth_token):
    allure.dynamic.story("携带 Token 获取用户信息")
    allure.dynamic.title("验证登录后获取的 Token 是否能正常访问受保护接口")
    
    # 1. 打印一下拿到的 Token
    print(f"\n拿到测试用的 Token :{auth_token}")
    assert auth_token is not None, "登录失败,未获取到Token"
    
    # 2. 带着 Token 去请求接口
    with allure.step("发送请求,携带 Authorization 头"):
        response_data = api_client.get_user_info(auth_token)
    
    # 3. 从返回的数据里，把服务器收到 Headers 提取出来
    received_headers = response_data["headers"]
    print(f"服务器收到的请求头:{received_headers}")
    
    # 4. 断言
    with allure.step("断言 Token 是否正确发送"):
        assert "Authorization" in received_headers
        assert received_headers["Authorization"] == f"Bearer {auth_token}"

      # 💡 下面是新加入的最高级断言：校验 JSON 数据结构
    with allure.step("断言 2:校验接口返回的 JSON Schema 结构"):
        # 定义你期望的数据结构类型
        expected_schema = {
            "type": "object",
            "properties": {
                "headers": {"type": "object"}
            },
            "required": ["headers"]  # 强制要求返回的数据里必须有 headers 字段
        }
        # 执行结构校验，如果返回的数据结构不对，这行代码会直接报错
        jsonschema.validate(instance=response_data, schema=expected_schema)  # type: ignore
       
    print("🎉 鉴权链路测试通过！")