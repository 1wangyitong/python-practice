import requests

class WeatherAPI:
    def __init__(self):
        # 1.初始化一个 Session 对象(相当于打开一个浏览器,保持 Cookie)
        self.session = requests.session()
        # 2.统一设置基础 URL ,以后换个环境(比如从测试环境到生产环境)只需要改这里
        self.base_url = "http://t.weather.itboy.net/api/weather/city"

    def get_weather(self,city_code):
        # 3.封装具体的请求方法
        url = f"{self.base_url}/{city_code}"
        response = self.session.get(url)
        return response.json()
    