import os
# 我们要把 httpbin.org（测试环境）和另一个环境（比如生产环境）区分开，并且支持一键切换。
#默认使用测试环境
ENV = os.getenv("MY_TEST_ENV","test")

class EnvConfig:
    #如果是在测试环境
    if ENV == "test":
        BASE_URL = "https://httpbin.org"
        DB_PATH = ":memory:"
    #如果是在生产环境(这里模拟)
    elif ENV == "prod":
        BASE_URL = "https://httpbin.org"# 真实工作中这里会换成正式的URL
        DB_PATH = "prod.db"
