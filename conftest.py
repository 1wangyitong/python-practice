
import pytest
from api.api_client import ApiClient

@pytest.fixture(scope="session")
def api_client():
    return ApiClient()

@pytest.fixture(scope="session")
def auth_token(api_client):
    # 整个会话只登录一次，拿到 token
    token = api_client.login("admin", "password")
    return token