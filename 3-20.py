# def calc(x, y):  # 形参-->只在函数内部有效
#     ret = x ** y
#     print(ret)
#
#
# a = 5
# b = 2
#
# calc(a, b)  # 实参


# def stu_register(name, age, course, country="CN"):   # 默认参数，放在后面
#     print("-------学籍信息注册-------")
#     print("姓名： ", name)
#     print("年龄： ", age)
#     print("国籍： ", country)
#     print("课程： ", course)

#
# stu_register("老王", 23, "C语言")
# stu_register("小李", 22, "JAVA", country="AM")  # 默认参数更改
# stu_register("王哥", 26, "数据库", "AU")    # 默认参数更改
# stu_register("张三", 21, "数据结构")


# # 非固定参数
# # *args: 会把多传入的参数变成一个元组形式  **kwargs  变成字典
# def stu_register(name, age, *args, **kwargs):
#     print(name, age, args, kwargs)
#
#     print(kwargs.get("addr"))  # 取
#
#
# # stu_register("DaoNan", 22)
# stu_register("Tom", 22, "Man", "C语言", addr="山东", hometown="德州")


#  函数返回值
#
def stu_register(name, age, course, country="CN"):
    print("-------学籍信息注册-------")
    print("姓名： ", name)
    print("年龄： ", age)
    print("国籍： ", country)
    print("课程： ", course)
    if age < 24:
        return True, age, course, country
    else:
        return False    # 程序一旦遇到return，就代表着函数的结束


register_info = stu_register("王哥", 23, "数据库", "AU")
print(register_info)
if register_info:
    print("注册成功")
else:
    print("年龄太大，不适合")


# name = "DaoNan"  # 全局变量 ：作用整个程序
#
#
# # 局部与全局同名时，在函数内局部起作用，在其他地方全局起作用
# def change_name():
#     #  global name  # 声明全局变量，不建议用，因为默认函数内不能修改全局变量
#     name = "隔壁老王"  # 局部变量：只在函数内部有效
#     print("改变后：", name)
#
#
# change_name()
# print("有变化吗？", name)

# 给函数传递列表list的现象

# d = {"name": "DaoNan", "age": 26, "hobbies": "足球"}
# l = ["老王", "小磊", "小哥"]
#
#
# def change_data(info, man):
#     info["hobbies"] = "篮球"
#     man.append("王哥")
#
#
# change_data(d, l)
# print(d, l)

# 常用内置函数
# # abs 取绝对值
#  print(abs(-10))

# # all 全部
# a = [1, 2, 3, 4, 5, 6]
# print(all(a))

# # any 任意一个值为True
# a = [1, 2, 3, 4, 5, 6]
# print(any(a))

# print(chr(122))  # 打印ASCII码值

# dict
#
# print(dict())  # 生成空字典
# print(dict(name="DaoNan"))
# dir 打印当前程序的所有变量名
# name = "DaoNan"
# age = 22
# print(__file__)
# print(dir())


#  打印当前作用域的所有变量名 和 变量值
# name = "DaoNan"
# age = 22
# print(locals())


# l = list(range(10))
# print(l)
#
#
# def calc(x):  # 只能定义一个参数
#     return x ** 2
#
#
# m = map(calc, l)  # 并未执行（迭代器）
# for i in m:  # 每循环一次，就把列表里的每一个元素扔给calc函数执行
#     print(i)


# max  最大值
# l = list(range(10))
# print(max(l))


# min
# l = list(range(10))
# print(min(l))
#
# # sum
# print(sum(l))


# # ord 打印ASCII 值
# print(ord("z"))
#

# # round 保留小数
# print(round(3.1415926, 2))


# zip 一一配对

# a = ["haha", "daddr", "jijiji"]
# b = ["AAA", "DDDD", "NNNN"]
#
# for i in zip(a, b):
#     print(i)

# # filter 把列表里的每一个元素交给第一个参数（函数）运行，若结果为真，则保留这个值
# l = list(range(10))
#
#
# def compare(x):
#     if x > 5:
#         return x
#
#
# print(l)
# for i in filter(compare, l):
#     print(i)


