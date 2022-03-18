# 字符编码：

# 1967年  Ascii： 0-->48   A-->65    z-->122

# 1980年  GB2312  一个中文两个字节

# 1991年  Unicode ：万国码，支持所有国家语言，效率低

# 1995年  GBK

# 1992年  UTF-8：最常用版本，一个中文占3个字节；还有不常用的 UTF-16，UTF-32

# python3： 存到文件里或者网络发送，用utf-8； 在内存里，依然是Unicode

#  mac/linux 默认是utf-8    windows在中国默认GBK

#  GBK --> utf-8 :   直接转成Unicode 或者  转成utf-8


#  文件操作

#  w  创建模式，只能写不能读，会覆盖原有文件
# f = open("name_list", mode="w")
#
# f.write("张三")
# f.write("李四")
# f.write("王二麻子")
#
# f.close()


# r  只读
# f = open("name_list", mode="r")
#
# print(f.read())  # 读所有
# print(f.readline())  # 读一行

#  a   追加模式  只能写，不能读
# f = open("name_list","a")
# f.write("haha")
# f.write("nono")
# # f.read()
# f.close()

#  遍历文件

# f = open("小姐姐联系方式")
#
# for line in f:
#     line = line.split()  #创建一个列表
# #   print(line)
#     height =int(line[3])
#     weight = int(line[4])
#     if height >= 170 and weight <= 50:
#         print(line)
#
# f = open("电影推荐.jpg", encoding="rb")  # rb 二进制只读
# print(f.read())

# wb 二进制写
# f = open("wb_file.txt", "wb")
#
# s = "DaoNan"
# f.write(s.encode("utf-8"))






