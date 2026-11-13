# def test_weather_with_frame(weather_api):
#     # 看！现在代码极其干净，一条 get 就拿到了所有数据
#     data = weather_api.get_weather("101010100")
    
#     city_name = data["cityInfo"]["city"]
#     print(f"\n框架封装后提取的城市:{city_name}")
#     assert city_name == "北京市"

import pytest
import yaml

def get_yaml_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# 读数据
test_data = get_yaml_data("weather_data.yaml")

@pytest.mark.parametrize("case", test_data)
def test_weather_with_frame(weather_api, case):
    city_code = case["city_code"]
    expected_city = case["expected_city"]
    
    data = weather_api.get_weather(city_code)
    city_name = data["cityInfo"]["city"]
    
    print(f"\n测试城市:{expected_city}，实际返回：{city_name}")
    assert city_name == expected_city