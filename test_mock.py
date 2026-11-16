import requests

def test_mock_login(mocker):
    # 1. 拦截 requests.post（这就是 Mock 魔法）
    mock_post = mocker.patch("requests.post")
    
    # 2. 伪造返回的假数据
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "msg": "登录成功", 
        "token": "fake_token_123456"
    }

    # 3. 发送请求（网址是假的，断网也不怕，因为被拦截了）
    response = requests.post("http://fake-website.com/login")
    
    print(f"\n拦截到的假状态码:{response.status_code}")
    print(f"拦截到的假数据：{response.json()}")
    
    # 4. 断言
    assert response.status_code == 200
    assert response.json()["token"] == "fake_token_123456"