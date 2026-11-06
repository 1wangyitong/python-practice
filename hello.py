import csv

# 1. 打开文件，注意这里用 utf-8-sig 解决刚刚的乱码问题
with open('test_data.csv', mode='r', encoding='utf-8-sig') as file:
    # 使用 DictReader，它会将每一行变成一个字典
    reader = csv.DictReader(file)
    
    # 2. 循环读取每一行
    for row in reader:
        # 提取字典里的 username 和 expected_status
        username = row['username']
        status = row['expected_status']
        
        # 3. 打印出要求的中文格式
        print(f"检查用户 {username} 的预期状态是 {status}")