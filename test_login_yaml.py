import yaml
import pytest
# 写一个辅助函数,专门用来读YAML文件
def get_yaml_data(file_path):
    with open(file_path,"r",encoding="utf-8") as f:
        # safe_load 会把 yaml 里面的数据转换成 Python 的列表/字典
        return yaml.safe_load(f)

# 调用函数,拿到数据表
test_data = get_yaml_data("login_data.yaml")

# 把读出来的数据直接喂给参数化装饰器
@pytest.mark.parametrize("case",test_data)
def test_login_by_yaml(case):
    username = case["username"]
    password = case["password"]
    expected_msg = case["expected_msg"]

    print(f"\n正在测试:账号{username},密码{password}")

    # 假设这里是真正发requests.post() 去请求登录接口
    # 我们这里先用简单逻辑模拟一下校验
    if len(password) < 6:
        actual_msg = "密码长度不能少于6位"
    elif not any(c.isalpha() for c in password) or not any(c.isdigit() for c in password):
        actual_msg = "密码必须包含字母和数字"
    else:
        actual_msg = "登录成功"
      # 断言：接口实际返回的提示，是否和 YAML 里写的预期一致
    assert actual_msg == expected_msg    