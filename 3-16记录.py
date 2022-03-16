
##  while循环:

# 死循环：
##count = 0
##while True:
##    count += 1
##    print(f"这是第{count}次循环...")


# 循环限制
##count = 0
##while count <= 10:
##    count += 1
##    print(f"这是第{count}次循环...")
##


#  while 猜年龄

##age_boy = 20
##
##count = 0
##while count < 3:
##    count += 1
##    guess = int(input("输入年龄："))
##
##    if guess > age_boy:
##        print("猜大了")
##    elif guess < age_boy:
##        print("猜小了")
##    else:
##        print("猜对了")



# 9*9 乘法表


##for i in range(1,10):
####    print(f"{i}x1={i*1}")
##
##    for j in range(1,i+1):
##        print(f"{i}x{j}={i*j}",end=" ") #  end 来控制空格
##    print()
##


#  京牌摇号小程序



#   random模块

import random
##random.choice("abcdef")  #随机抽出一个值
##
##a = "acbdhdj"
##
##random.sample(a,3)

##random.randint(1,100)
##
##
#  string 模块



##
##import random
##import string
##
##count = 0;
##while count < 3:
##    car_nums = []  #存储供用户选择的号
##
##    for i in range(20):
##        n1 = random.choice(string.ascii_uppercase)  #生成车牌第一个字母
##        n2 = "".join(random.sample(string.ascii_uppercase+string.digits,5))
##        c_num = f"京{n1}-{n2}"
##        car_nums.append(c_num)   #把生成的号码添加到列表
##        print(i+1,c_num)
##    choice = input("输入你喜欢的号：").strip()
##    if choice in car_nums:
##        print(f"恭喜你选择了新牌号：{choice}")
##        exit("GoodLuck.")
##    else:
##        print("不合法选择")
##
##    count += 1
##        
##



#  数据类型

#  字符串

##s = "hello world"    
##
##s[3:6]   #切片操作

#常用操作

a = "hello world"

print(a.center(50,"-"))  # 打印：-------------------hello world--------------------

print(a.count("l")) # 计数字符出现次数

print(a.endswith("d"))  # 判断结尾

print(a.startswith("h"))

print(a.find("e")) # 字符查找 返回1/-1

print(a.isdigit())
print("22".isdigit())  #  判断是否是整数


b = ["nonoono","heheheh","gagagaga"]
print("-".join(b))  # 拼接字符串

print(a.replace("o","t",1))  # 字符串替换

print(a.split("l"))     #  分割字符串

























