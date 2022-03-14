# 开始

#程序员的开始 hello world

# print("Hello world")

'''
cpu  只负责计算

内存  临时数据存储

硬盘   数据存储

'''

'''
1. 变量

定义后调用
'''
'''
name = "haha"

print(name)

# 修改直接改
name = "nono"

print(name)

#删除

del name

'''
'''
尽量定义在开头；字母，数字，下划线组合；数字不能开头
区分大小写；关键字不能作为变量




2.数据类型: 可用 type(变量名) 查看类型

整数  int  
浮点  float 
字符串 双引号/单引号     三引号（三单或三双）：多行字符串
'''

'''
name1 = "hello"
name2 = name1.upper() # 转换为大写
print(name2)
name3 = name2.lower()  #转换为小写
print(name3)
name4 = name3.center(50,"-")
print(name4)

name5 = name2 + name3  #字符串拼接（可以+，可以*）
print(name5)

'''
'''
布尔   True False  用来逻辑判断

列表   一个变量存多种数据   names = ["元素1"，"元素2"，"元素3"]
                            通过下标标记元素位置，从0开始
例：插入 names.insert(index,"元素")
    尾部追加 names.append("元素")
    删除  del names[index]  或  names.remove("元素")：若有重名，从左边开删
    判断  in  查看元素是否在列表里
元组 字典 集合

'''


