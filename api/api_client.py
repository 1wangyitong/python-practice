import requests
from config import EnvConfig
class ApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = EnvConfig.BASE_URL
        
        # 🚀 新增：配置代理，让 requests 像浏览器一样通过梯子出国
        self.proxies = {
            "http": "http://127.0.0.1:7897",
            "https": "http://127.0.0.1:7897",
        }
    def get_weather(self, city_code):
        url = f"http://t.weather.itboy.net/api/weather/city/{city_code}"
        response = self.session.get(url, timeout=5)
        return response.json()

    def login(self, username, password):
        url = f"{self.base_url}/basic-auth/{username}/{password}"
        # 这里加上 proxies=self.proxies
        response = self.session.get(url, auth=(username, password), proxies=self.proxies)
        if response.status_code == 200:
            return "fake_token_123456"
        return None

    def get_user_info(self, token):
        url = f"{self.base_url}/headers"
        headers = {"Authorization": f"Bearer {token}"}
        # 这里也加上 proxies=self.proxies
        response = self.session.get(url, headers=headers, proxies=self.proxies)
        return response.json()