import requests
def test_get_post():
# 1. 发送 GET 请求获取 id 为 1 的帖子
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
 # 2. 把服务器返回的 JSON 转换成 Python 字典
    data = response.json()
    print(f"服务器返回的数据是：\n{data}")
# 3. 写断言（Pytest的灵魂）
    assert response.status_code == 200
    assert data["id"] == 1
    assert "title" in data  # 断言返回的数据里一定有标题


# 用post方法模拟新建数据
def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    # 准备要发送的测试数据（字典格式）
    payload = {
    "title": "测试开发日记",
    "body": "今天学会了requests和断言",
    "userId": 1
    }
# 发送 POST 请求，用 json=payload 把数据传过去
    response = requests.post(url, json=payload)
    data = response.json()
 # 打印看看服务器返回了什么
    print(f"\n新建成功，服务器返回的数据是：{data}")
    
    # 断言
    assert response.status_code == 201 # POST 新建成功的状态码通常是 201
    assert data["title"] == "测试开发日记" # 检查返回的数据里，标题对不对    
    