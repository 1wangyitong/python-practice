import requests
from jsonpath import jsonpath 
def test_weather_beijing():
    url="http://t.weather.itboy.net/api/weather/city/101010100"
    response = requests.get(url)
    #1.断言状态码
    assert response.status_code == 200
    data = response.json()
    # (方法一)2. 提取数据：字典["key"] 或 列表[索引]
    # 获取城市名称
    city_name = data["cityInfo"]["city"]
    #  获取今天（forecast列表第1个元素）的最高温度和天气状况
    # today_high = data["data"]["forecast"][0]["high"]
    # today_type = data["data"]["forecast"][0]["type"]
    # 获取昨天的最高温度和天气状况
    # today_high = data["data"]["forecast"][1]["high"]
    # today_type = data["data"]["forecast"][1]["type"]


    #(方法二) 2. 用 jsonpath 提取数据
    # "$..high" 的意思是：不管嵌套多深，把所有的 high 字段都抓出来，返回一个列表
    high_list = jsonpath(data, "$..high")
    # 取列表里的第一个（也就是今天的最高温）
    today_high = high_list[0] 
    # 同理，抓取所有的 type (天气状况)
    type_list = jsonpath(data, "$..type")
    today_type = type_list[0]
    # 抓取城市名
    city_list = jsonpath(data, "$..city")
    city_name = city_list[0]


    # 3. 打印出来看看
    print(f"\n城市:{city_name}")
    print(f"今日最高温:{today_high}")
    print(f"今日天气:{today_type}")
    
    # 4. 写断言，验证提取到的数据是否符合预期
    assert city_name == "北京市"
    assert "℃" in today_high  # 最高温里应该包含温度符号
    assert today_type != ""   # 天气状况不能为空    