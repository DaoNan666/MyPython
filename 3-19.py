#  混合模式文件操作
#  w+ 写读   r+ 读写，写在文件后面   a+  追加读
# f = open("小姐姐联系方式", "r+")
# print(f.read())
# print(f.tell())  # 237
# f.seek(f.tell())  # 不加会默认在文件后直接加
# f.write("哦买嘎")


#  文件修改：不是覆盖，而是往后挤

# f = open("小姐姐联系方式", "r+")
#
# # 1. 加载到内存
# data = f.read()
# new_data = data.replace("岳妮妮", "haha")
#
# # 2.清空文件
# f.seek(0)
# f.truncate()  # 截断文件
#
# # 3. 把新内容写回硬盘
# f.write(new_data)
# f.close()

# 全局文本检索替换
# import sys
#
# print(sys.argv)
# old_str = sys.argv[1]
# new_str = sys.argv[2]
# filename = sys.argv[3]
# # 1. 加载到内存
# f = open(filename, "r+")
# data = f.read()
# # 2. 计数和替换
# old_str_count = data.count(old_str)
# new_data = data.replace((old_str, new_str))
# # 3.清空文件
# f.seek(0)
# f.truncate()
# # 4.把新内容写到文件
# f.write(new_data)
# f.close()
# print(f"成功替换字符‘{old_str}'to'{new_str}',共{old_str_count}处...")

#  用户登录程序

# 1.确定 在文件里存储的账号信息结构

# 2. 把数据读到内存，为方便调用，改成列表结构list或字典
accounts = {

}
f = open("account.db", "r")
for line in f:
    line = line.strip().split(",")  # strip 吃空格
    accounts[line[0]] = line

# 3. 搞个循环。要求用户输入信息，判断

while True:
    user = input("Username:").strip()
    if user not in accounts:
        print("该用户未注册...")
        continue
    elif accounts[user][2] == "1":
        print("该账户已锁定，请联系客服解决...")
        continue
    count = 0
    while count < 3:  # 控制密码输入次数
        passwd = input("Password:").strip()
        # 去账号的字典里判断密码是否正确
        if passwd == accounts[user][1]:
            print(f"Welcome{user}...登录成功...")
            exit("bye bye...")
        else:
            print("密码错误....")
        count += 1
    if count == 3:
        print(f"输错了{count}次密码，锁定账号{user}...")
        # 1.先改内存中字典里的账号信息的用户状态
        # 2.把字典里的数据信息按源数据格式存回文件
        accounts[user][2] = "1"   # 1代表账户锁定
        f2 = open("account.db", "w")
        for user, val in accounts.items():
            line = ",".join(val) + "\n"
            f2.write(line)
        f2.close()

        exit("bye bye...")

#  函数: 减少重复代码；  使程序变得可扩展；  使程序变得易维护

# def Add():  # 函数名
#     print("这是加法")
#
#
# Add()  # 调用函数
#
#
# def Add(a, b):  # 带参数
#     c = a + b
#     print(c)
#
#
# Add()

# def hello(name, age):
#     print(f"hello,my name is {name},this year {age} years old..")
#
#
# hello("DaoNan", "22")
