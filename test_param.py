import requests
import pytest
# 用装饰器准备 3 组测试数据
@pytest.mark.parametrize("post_id, expected_user_id", [
    (1, 1),  # 第一组：查 id 1，预期 userId 是 1
    (2, 1),  # 第二组：查 id 2，预期 userId 也是 1
    (3, 1)   # 第三组：查 id 3，预期 userId 也是 1
])
# def test_posts_with_different_ids(post_id, expected_user_id):
#     # 把传进来的 post_id 拼接到 URL 里
#     url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
#     response = requests.get(url)
#     data = response.json()
    
#     print(f"\n正在测试帖子 ID: {post_id}")
    
#     assert response.status_code == 200
#     # 断言传进来的预期结果
#     assert data["userId"] == expected_user_id 
# 以上注释的第9行到第19行,是 任务二：学会 Pytest 的“大招”——参数化(块1 核心)
def test_posts_with_different_ids(base_url, post_id, expected_user_id): # <--- 看这里！把 base_url 当参数传进来了
    # 现在不需要写死长网址了，直接用 base_url 变量拼接
    url = f"{base_url}/posts/{post_id}"
    response = requests.get(url)
    data = response.json()
    
    assert response.status_code == 200
    assert data["userId"] == expected_user_id
