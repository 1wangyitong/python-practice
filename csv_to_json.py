import csv
import json

# 准备一个空列表，用来装读取出来的数据
data_list = []

# 读取 CSV
with open('test_data.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # 把每一行（字典）塞进大列表里
        data_list.append(row)

# 将列表保存为 JSON 文件
with open('output.json', mode='w', encoding='utf-8') as json_file:
    # ensure_ascii=False 让中文正常显示；indent=4 让格式好看
    json.dump(data_list, json_file, ensure_ascii=False, indent=4)

print("转换成功！数据已经保存到 output.json 里了。")