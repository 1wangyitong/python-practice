print("欢迎来到测试用例优先级设置系统")
while True:
    try :
       user_input = input("请输入 1-100 之间的数字作为优先级: ")
       priority = int(user_input)
       if 1 <= priority <= 100:
            print(f"✅ 优先级已成功设置为：{priority}")
            break  # 输入正确，跳出循环
       else:
            print("❌ 错误：数字必须在 1 到 100 之间，请重新输入！")
            
    except ValueError:
        print("❌ 错误：你输入的不是数字，请重新输入！")

print("程序结束，可以开始执行你的测试用例了。")