import pytest

# 模拟你们公司后端的密码校验函数
def check_password(password):
    # 规则：长度 6-16，必须同时包含字母和数字
    if len(password) < 6 or len(password) > 16:
        return False
    
    # 检查是否所有字符都是字母或数字（如果有特殊符号，这里就是False）
    if not password.isalnum(): 
        return False
        
    # 检查是否包含字母
    has_letter = any(c.isalpha() for c in password)
    # 检查是否包含数字
    has_digit = any(c.isdigit() for c in password)
    
    return has_letter and has_digit

# 把你在纸上写的测试点，用参数化写出来
@pytest.mark.parametrize("password, expected_result, case_description", [
    # --- 有效等价类 ---
    ("12345a", True, "6位,字母+数字"),
    ("1234abcd", True, "8位,字母+数字"),
    ("12345678901234ab", True, "16位,`字母+数字"),
    
    # --- 无效等价类 ---
    ("123456", False, "纯数字"),
    ("abcdefg", False, "纯字母"),
    ("abc!@#123", False, "包含特殊符号"),
    ("", False, "空值"),
    
    # --- 边界值 ---
    ("1234a", False, "5位(少一位)"),
    ("12345a", True, "6位(最短边界)"),
    ("123456789012345a", True, "16位(最长边界)"),
    ("1234567890123456a", False, "17位(多一位)")
])
def test_password_rules(password, expected_result, case_description):
    print(f"\n正在测试用例: {case_description}，数据: {password}")
    assert check_password(password) == expected_result