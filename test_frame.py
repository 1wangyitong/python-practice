def test_weather_with_frame(weather_api):
    # 看！现在代码极其干净，一条 get 就拿到了所有数据
    data = weather_api.get_weather("101010100")
    
    city_name = data["cityInfo"]["city"]
    print(f"\n框架封装后提取的城市:{city_name}")
    assert city_name == "北京市"