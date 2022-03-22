#  模块编程

#  模块： 提高代码可维护性；  避免函数名和变量名冲突

#  分类：   内置标准模块（标准库）；   第三方开源模块；  自定义模块

#  调用：
# import os  # 导入
#
# from os import system  # 导入某个模块下的某个方法 或 子模块
#


# 自定义模块（注意模块路径）

# 第三方开源库： 网站：https://pypi.org/，可命令行安装
#             若pycharm慢，可改镜像源


# 包的使用（__init__.py)
#  os  常用
# import os
#
# os.getcwd()  # 获取当前路径
#
# os.listdir()  # 获取所有文件和目录名
#
# os.remove()  # 删除一个文件
#
# os.removedirs()  # 删除多个目录
#
# os.path.isfile()  # 检验给出的路径是否是一个文件
#
# os.path.isdir()  # 检验给出的路径是否是一个目录
#
# os.path.exists()  # 检验给出的路径是否真的存在
#
# os.path.dirname()  # 获取路径名
#
# os.path.abspath()  # 获取绝对路径
#
# os.path.basename()  # 获取文件名
#
# os.system()  # 运行shell命令
#
# os.renames(old,new)  # 重命名
#
# os.makedirs()  # 创建多级目录
#
# os.mkdir()  # 创建单个目录
#
# os.stat()  # 获取文件属性
#
# os.path.getsize()  # 获取文件大小

#  time模块

#  时间戳   格式化的时间字符串   元组

# import time

# print(time.time())  # 返回当前时间戳
#
# print(time.localtime())  #  将时间戳 转换 当前时区的struct_time
#
# print(time.gmtime())  #  转换 UTC时间（0时区）

# print(time.mktime(time.localtime()))  # 将时区 转换回 时间戳

# print(time.strftime("%Y-%m-%d %H:%M:%S %p"))  # 转换为格式化时间字符串
#
# time_str = time.strftime("%Y-%m-%d %H:%M:%S")
# print(time.strptime(time_str, "%Y-%m-%d %H:%M:%S"))  # 转换回日期格式

# datetime 模块

# import datetime
# print(datetime.datetime.now())  # 打印当前时间
#
# print(datetime.datetime.now() + datetime.timedelta(5, hours=4))  # 当前时间加5天4小时
#
# d = datetime.datetime.now()
# print(d.replace(year=2025, month=9))  # 时间替换：当前时间改为2025年9月
# random 模块
# import random
#
# print(random.randrange(1, 10))  # 返回1-10之间一个随机数，不包括10
#
# print(random.randint(1, 10))  # 返回1-10之间一个随机数，包括10
#
# print(random.randrange(0, 100, 2))  # 随机返回0-100之间一个偶数
#
# print(random.random())  # 返回随机浮点数
#
# print(random.choice('adadjidjijs%#'))  # 返回给定字符串中随机字符
#
# print(random.sample('sadadaidjiw', 2))  # 返回特定数量字符

# excel 处理
# 创建
# from openpyxl import Workbook, load_workbook

#
# wb = Workbook()
# sheet = wb.active
#
# print(sheet.title)
# sheet.title = "处理表格"
#
# #  写数据
# sheet["B9"] = "DaoNan"
# sheet["C9"] = "22岁"
#
# sheet.append(["老鹅", "21岁"])
#
#
#
# wb.save("excel_test.xlsx")

# 打开
# wb = load_workbook("excel_test.xlsx")

# 打开操作
# wb = load_workbook("考试安排.xlsx")
#
# print(wb.sheetnames)
# print(wb.get_sheet_names())
# sheet = wb.get_sheet_by_name("专业课")

# print(sheet["D6"])
# print(sheet["D6"].value)

# for cell in sheet["E6:E10"]:     # 获取制定列的切片数据
#     print(cell[0].value)

# for row in sheet:  #  打印全部
#     print(row)
#     for cell in row:
#         print(cell.value,end=",")
#
#     print()


# 指定区域打印
#
# for row in sheet.iter_rows(min_row=7,max_row=21,max_col=5):
#     for cell in row:
#         print(cell.value,end=",")
#
#     print()


# 按列遍历
# for col in sheet.columns:
#     for cell in col:
#         print(cell.value,end=",")
#
#     print()
#  修改
# sheet["D5"] = "DaoNan"

#  花式操作：改字体，颜色，加粗等
# from openpyxl.styles import Font, colors, Alignment
#
# myfont = Font(name="宋体", size=20, italic=True, color=colors.BLUE)
#
# sheet["D5"].font = myfont
#
# wb.save("考试安排.xlsx")




