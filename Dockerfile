# 基础镜像：使用官方轻量级 Python 3.10
FROM python:3.10-slim

# 设置容器内的工作目录为 /app
WORKDIR /app

# 拷贝依赖清单
COPY requirements.txt .

# 安装依赖（使用阿里云镜像加速）
RUN pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# 拷贝当前目录所有代码到容器的 /app 下
COPY . .

# 运行测试命令
CMD ["pytest"]