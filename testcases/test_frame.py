# def test_weather_with_frame(weather_api):
#     # 看！现在代码极其干净，一条 get 就拿到了所有数据
#     data = weather_api.get_weather("101010100")
    
#     city_name = data["cityInfo"]["city"]
#     print(f"\n框架封装后提取的城市:{city_name}")
#     assert city_name == "北京市"

import pytest
import yaml
import os
import allure

def get_yaml_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 读数据
test_data = get_yaml_data("data/weather_data.yaml")

@allure.feature("天气服务模块")  # 第一层：大模块
@pytest.mark.parametrize("case", test_data)
def test_weather_with_frame(api_client, case):
    city_code = case["city_code"]
    expected_city = case["expected_city"]
    
    # 第二层：具体场景（必须在函数内部调用 dynamic 才能用变量）
    allure.dynamic.story("查询指定城市天气")
    allure.dynamic.title(f"测试城市代码: {city_code}")
    
    # 发送请求（黄色波浪线是编辑器的提示，不用管，能跑就行）
    data = api_client.get_weather(city_code)
    city_name = data["cityInfo"]["city"]
    
    # 💡 附加请求参数和响应数据到报告里
    allure.attach(
        str(city_code),
        name="请求参数 (city_code)",
        attachment_type=allure.attachment_type.TEXT
    )
    allure.attach(
        str(data),
        name="服务器返回的完整JSON",
        attachment_type=allure.attachment_type.JSON
    )
    
    print(f"\n测试城市:{expected_city}, 实际返回: {city_name}")
    assert city_name == expected_city