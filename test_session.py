
import requests

def test_use_session():
    # 1. 创建一个 Session 对象（就像打开了一个浏览器）
    session = requests.Session()
    
    # 2. 用 Session 发送第一次请求（模拟登录或获取验证信息）
    # 这里我们随便请求一个接口
    session.get("https://jsonplaceholder.typicode.com/users/1")
    
    # 3. 用同一个 Session 发送第二次请求
    # 真实场景中，第二次请求会自动带上第一次请求留下的 Cookie
    response = session.get("https://jsonplaceholder.typicode.com/posts/1")
    
    assert response.status_code == 200
    print("\nSession 会话保持成功！")