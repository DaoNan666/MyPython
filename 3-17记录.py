# 列表

# names=['DaoNan','Boy','python','java','world']
# print(names)
# names.append('haha')   #添加
# print(names)
#
# names.append(''play)
# print(names)

# names.insert(2,'nono')  #插入
# print(names)
#
# a = ['beautiful girl']
# names.extend(a)  #合并
# print(names)
#
# del names[2]  #删除
# print(names)
#
# names.pop()  #默认删除最后一个
# print(names)
#
# deleted_item = names.pop()
# names.pop(-2)
# print(names)
#
# names.remove('haha')
# print(names)
#
# names.clear()  #清空
# print(names)


# a = names.index('haha')  #查
# print(a)
#
# a = names.count('haha') # 计个数
# print(a)

# a = names[1:4]   #切片
# print(a)

# a = names[-3:-1]  # 倒着切
# print(a)

# a = names[0:-1:2]  # 跳着切
# print(a)

# names.sort()  #排序
# print(names)
#
# names.reverse()  # 反转
# print(names)

# for i in names:   #列表循环
#     print(i)
#
# for i in enumerate(names):   #索引
#     print(i)


# 班级成员分组小程序


stu_list = [ ['小王',82],['李世民',90],['唐太宗',34],['杨贵妃',56],['貂蝉',66],
             ['武松',78],['蒋锡培',34],['刘东华',100],['科特勒',78],['惠茜',66],
             ['梦璐',97],['李朝曙',94],['陈志列',67],['姚日来',45],['博容',88],
             ['博易',83],['易烟',0],['以蕊',100],['曼文',26],['痴珊',69],
             ['初夏',77],['安民',73],['智志',62],['子民',84],['子墨',93],['雅静',96]]
stu_groups = [
    [],  #90-100
    [],  #80-90
    [],   #70-79
    [],   #60-69
    [],   #0-59
]


for i in stu_list:
    if i[1] >= 90:
        stu_groups[0].append(i)
    elif i[1] >= 80:
        stu_groups[1].append(i)
    elif i[1] >= 70:
        stu_groups[2].append(i)
    elif i[1] >= 60:
        stu_groups[3].append(i)
    else:
        stu_groups[4].append(i)
for i in stu_groups:
    print(i)


#   字典

# dict   --   key-value 结构

# dic = {
#     "xiao": [23, "总裁", 9000],
#     "wang": [54, "员工", 6000],
#     "gang": [35, "经理", 6600]
# }

# print("wang" in dic)
#
# print(dic["wang"])  # 拿出数据

# 注意： key必须是不可改变数据类型，必须唯一；value可修改；
#       无序；查询速度快；


# dic = {
#     "xiao": [23, "总裁", 9000],
#     "wang": [54, "员工", 6000],
#     "gang": [35, "经理", 6600]
# }

# print(dic["xiao"])  # 取出
#
# print('wang' in dic)  # 查找
#
# a = dic.keys()
# print(a)
#
# for i in dic.keys():  # 循环
#     print(i)

# for k in dic:   # 官方循环，效率高
#     print(k, dic[k])

# a = dic.values()
# print(a)
#
# a = dic.items()
# print(a)

# a = len(dic)   # 求长度，可用于字典，列表，字符串
# print(a)
