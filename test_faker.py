from faker import Faker

# 初始化，指定生成中文数据
fake = Faker('zh_CN')

def test_fake_data():
    print("\n--- 生成伪造测试数据 ---")
    # 循环3次生成3个假用户
    for _ in range(3):
        name = fake.name()
        phone = fake.phone_number()
        id_card = fake.ssn(min_age=18, max_age=60)
        print(f"姓名: {name} | 手机: {phone} | 身份证: {id_card}")