# -*- coding = utf-8 -*-
# @Time : 2022/4/11
# @Author : 道南
# @File : day-12.py
# @Software : PyCharm

#  for 循环
# for i in range(5):
#     print(i)   # 输出 0 1 2 3 4
#
# for i in range(0, 10, 3):
#     print(i)  # 输出 0 3 6 9
#
# for i in range(-10, -100, -30):
#     print(i)  # 输出 -10 -40 -70
#
# name = "daonan"
# for i in name:
#     print(i, end="\t")  # 输出d a o n a n
#
# a = ["aa", "bb", "cc", "dd"]
# for i in range(len(a)):
#     print(i, a[i])  # 输出 0 aa 1 bb 2 cc 3 dd


#  while 循环
# i = 0
# while i < 5:
#     print("当前是第%d次执行循环" % (i + 1))
#     print("i=%d" % i)
#     i += 1
# 输出结果：
# 当前是第1次执行循环
# i=0
# 当前是第2次执行循环
# i=1
# 当前是第3次执行循环
# i=2
# 当前是第4次执行循环
# i=3
# 当前是第5次执行循环
# i=4


# # 1-100 求和
# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
# print("1到%d的和为：%d" % (n, sum))

# count = 0
# while count < 5:
#     print(count, "小于5")
#     count += 1
# else:
#     print(count, "大于或等于5")

# 输出结果：
# 0 小于5
# 1 小于5
# 2 小于5
# 3 小于5
# 4 小于5
# 5 大于或等于5


# break continue pass

# i = 0
# while i < 10:
#     i += 1
#     print("-"*30)
#     if i == 5:
#         break  # 结束整个循环
#     print(i)

# i = 0
# while i < 10:
#     i += 1
#     print("-"*30)
#     if i == 5:
#         continue  # 结束本次循环
#     print(i)
#

# 输出99乘法表

# # 方法一：
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j}x{i}={i * j}\t', end=" ")
#     print()
#
# #方法二：
# i = 1
# while i <= 9:
#     j = 1
#     while (j <= i):
#         print(f'{i}*{j}={i * j}', end='\t')
#         j += 1
#     print('')
#     i += 1

# 字符串  可以单引号  双引号  三引号

# a = '字符串'
# b = "这是一个句子"
# c = """
#   我哈哈哈哈
#   我呵呵呵呵
# """
# print(a)
# print(b)
# print(c)

# 区分单引号 双引号

# # my_str = "I'm a student"
# my_str = 'I\'m a student'
# print(my_str)
#
# # my_str = "daonan said:\"I‘m a student\""
# my_str = 'daoan said:"I’m a student'
# print(my_str)

# 字符串的截取

# str = "daonan666"
# print(str)
# print(str[0:7])  # [起始位置 : 结束位置]
# print(str[1:9:2]) # 输出ann6
# print(str[:6])
# print(str[6:])
#
# print(str + "good")  # 字符串连接
# print(str * 3)
#
# print("hello\nworld")  # 转义字符换行
# print(r"hello\nworld")  # 在字符串前加r，则显示原始字符串

# 列表 list

# # namelist = []  #  定义一个空列表
#
# namelist = ["小王", "小磊", "小草"]
# print(namelist[0])
#
# namelist = [22, "小王", "五年级"]  # 可以存储不同类型
# print(namelist[0])
# print(namelist[1])
# print(namelist[2])
#
# namelist = [22, "小王", "五年级"]
# for name in namelist:
#     print(name)
# print(len(namelist))  # 求列表长度

# 增 删 改 查

# namelist = [22, "小王", "五年级"]
# print("--------增加前，名单列列表数据-------")
# for name in namelist:
#     print(name)
# nametemp = input("请添加课程：")
# namelist.append(nametemp)  # 在末尾追加一个元素
#
# print("--------增加后，名单列列表数据-------")
# for name in namelist:
#     print(name)

# a = [1, 2]
# b = [3, 4]
# a.append(b)  # 整体加入
# print(a)
#
# a = [1, 2]
# b = [3, 4]
# a.extend(b)   # 在a后直接扩展，将b中每一个元素逐一追加到列表中
# print(a)
#
# a = [0, 1, 2]
# a.insert(1, 3)  # 第一个变量为下标  第二个变量为元素
# print(a)  # 输出[0, 3, 1, 2]

# moviename = ["霸王别姬", "让子弹飞", "活着", "笑傲江湖：东方不败", "A计划"]
# print("--------删除前，电影列列表数据-------")
# for name in moviename:
#     print(name)
#
# # del moviename[2]  # 在指定位置删除元素
# # moviename.pop()  # 弹出末尾最后一个元素
# moviename.remove("让子弹飞")  # 删除指定内容元素，若列表内容出现重复，会删除找到的第一个元素
#
# print("--------删除后，电影列列表数据-------")
# for name in moviename:
#     print(name)

# namelist = [22, "小王", "五年级"]
# print("--------修改前，名单列列表数据-------")
# for name in namelist:
#     print(name)
#
# namelist[1] = "小磊"   # 修改制定下标数据
#
# print("--------修改后，名单列列表数据-------")
# for name in namelist:
#     print(name)

# namelist = ["小王", "小磊", "小草"]
# findname = input("请输入要查找的姓名：")
# if findname in namelist:
#     print("该学生在学员列表中")
# else:
#     print("该学生不在学员列表中")
#
# mylist = ["a", "b", "c", "a", "b"]
#
# print(mylist.index("a", 1, 4))  # 可以查找指定下标范围的元素，并返回找到对应数据的下标
#
# print(mylist.index("a", 1, 3))  # 报错，范围区间，左闭右开 [1, 3)
#
# print(mylist.count("b"))  # 查找列表中某个元素出现次数


# a = [1, 5, 7, 2]
# print(a)
# a.reverse()  # 将列表所有元素反转
# print(a)
#
# a.sort()  # 排序-升序
# a.sort(reverse=True)  # 降序
# print(a)


# schoolname = [["清华大学", "北京大学"], ["山东大学", "曲阜师范大学", "济南大学"], ["天津大学", "南开大学"]]
#
# print(schoolname[0][0])  # 输出 清华大学


# import random
#
# offices = [[], [], []]
#
# names = ["A", "B", "C", "D", "E", "F", "G", "H"]
# for name in names:
#     index = random.randint(0, 2)
#     offices[index].append(name)
# i = 1
# for office in offices:
#     print("办公室%d人数为：%d" % (i, len(office)))
#     i += 1
#     for name in office:
#         print("%s" % name, end="\t")
#     print("\n")
#     print("-"*20)


# 元组

# tup1 = ()  # 创建一个空的元组
# print(type(tup1))
#
# tup2 = (50,)  # 加逗号
#
# print(type(tup2))


# tup1 = ("abc", "def", 2022, 3)
# print(tup1[0])
# print(tup1[-1])  # 访问最后一个元素
# print(tup1[1:4])  # 左闭右开，进行切片

#  增 删  改(不允许修改） 查
#
# tup1 = (12, 34, 56)
# tup2 = ("abc", "def")
#
# tup = tup1 + tup2  # 连接
#
# print(tup)
#
# tup1 = (12, 34, 56)
# print(tup1)
# del tup1  # 删除整个元组变量，不能删除某个值
# print("删除后：")
# print(tup1)


# 字典 键-值（key-value）
#
# info = {"name": "道南", "age": 22}  # 字典的定义
# print(info["name"])
# print(info["age"])

# # 增
#
# info = {"name": "道南", "age": 22}
# newid = input("输入学号：")
# info["id"] = newid
# print(info["id"])

# 删

# info = {"name": "道南", "age": 22}
# print("删除前：%s" % info["name"])
# del info["name"]  # 删除整个键值对
# print("删除后：%s" % info["name"]) # 报错

# info = {"name": "道南", "age": 22}
# print("删除前：%s" % info)
# del info
# print("删除后：%s" % info) # 报错
#
# 清空
#
# info = {"name": "道南", "age": 22}
# print("清空前：%s" % info)
# info.clear()
# print("清空后：%s" % info)

# 改
#
# info = {"name": "道南", "age": 25}
#
# info["age"] = 22
#
# print(info["age"])


# 查
#
# info = {"id": 1, "name": "道南", "age": 25}
# print(info.keys())  # 得到所有的键
# print(info.values())  # 得到所有的值
# print(info.items())  # 得到所有的项，每个键值对是一个元组


# 遍历所有的值
# info = {"id": 1, "name": "道南", "age": 25}
# for key in info.keys():  # 遍历所有的键
#     print(key)
#
# for value in info.values():  # 遍历所有的值
#     print(value)
#
# for key,value in info.items():  # 遍历所有的项
#     print("key=%s, value=%s" % (key, value))

# 使用枚举函数同时拿到列表中的下标和内容
#
# mylist = ["a", "b", "c"]
# for i, x in enumerate(mylist):
#     print(i, x)  # 获取下标和内容
