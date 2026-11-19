import sqlite3
import pytest
from faker import Faker

fake = Faker('zh_CN')

# 模拟被测系统的数据库
def init_db():
    conn = sqlite3.connect(':memory:') # 在内存中创建一个数据库
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, phone TEXT)''')
    conn.commit()
    return conn
#模拟真实的注册接口操作（底层会写库）
def mock_register_api(conn,username,phone):
    cursor = conn.cursor()
    #相当于 INSERT INTO user...
    cursor.execute("INSERT INTO users(username,phone) VALUES(?,?)",(username,phone))
    conn.commit()
    return{"code":200,"msg":"注册成功"}
def test_register_and_db_verify():
    # 1.准备环境和假数据
    conn = init_db()
    random_name = fake.name()
    random_phone = fake.phone_number()
    #2.调用接口进行注册
    res = mock_register_api(conn,random_name,random_phone)
    assert res["code"] == 200
    #3.核心来了 去数据库里校验(DB Assertion)
    cursor = conn.cursor()
    #使用 SELECT 语句查询刚才注册的用户
    cursor.execute("SELECT username,phone FROM users WHERE phone = ?",(random_phone,))
    db_result = cursor.fetchone()

    print(f"\n接口请求生成的用户:{random_name},手机号:{random_phone}")
    print(f"数据库查到的用户:{db_result[0]},手机号:{db_result[1]}")

    #4.断言:接口返回的和数据库存的一定要一致
    assert db_result is not None,"数据库里没有查到该用户!"
    assert db_result[0] == random_name,"数据库里的名字和发送的不一致"

