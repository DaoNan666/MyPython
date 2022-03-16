'''运算符

* 乘      x**y 返回x的y次幂
/ 除        // 取整除

逻辑运算  and: 全真为真   or：有真就真  not :取反

成员运算 :可以测试字符串，列表，元组，字典，集合，不能测试数字类型
         in       not in

'''

#  读取用户输入
#  input:读的值都是字符串，即使你输入的是数字（要类型转换）
'''
name = input("name:")
age = input("age:")
hometown = input("hometown：")

print(name)
print(age)
print(hometown)

'''
#  格式化打印

#  流程控制
#  单分支
'''
salary = 8000
if salary < 1000:
    print("哈拉少")
else:
    print("无情")
print("hh")
'''
#  双分支
'''
salary = 8000
if salary < 1000:
    print("哈拉少")
else:
    print("无情")
'''
#  缩进  tab 替换4个空格
'''
顶级代码必须顶行写；同一级别的代码，缩进必须一致
官方建议4个空格

'''
#  多分支

'''
age_of_boy = 48
guess = int(input("输入年龄："))
if guess > age_of_boy:
    print("猜大了") 
elif guess < age_of_boy:
    print("猜小了")   
else:
    print("猜对了")

'''
#  for循环

##for i in range(10):
##    print(i)
##
##
##for i in range(5,10):
##    print(i)

##
##age_of_boy = 48
##for i in range(3): 
##    guess = int(input("输入年龄："))
##    if guess > age_of_boy:
##        print("猜大了") 
##    elif guess < age_of_boy:
##        print("猜小了")   
##    else:
##        print("猜对了")


# 循环嵌套
##
##for i in range(1,6):
##
##    for j in range(1,9):
##
##        print(f"L{i}-{i}0{j}室")



##for i in range(1,6):
##    print(f"----------{i}层---------")
##    if i == 3: #  若为3，跳过本次循环，进入下一次
##            continue
##    for j in range(1,9):
##        if i == 4 and j == 4:
##            print("遇到鬼屋404了....")
##            break  # 结束当前循环
##        
##        print(f"L{i}-{i}0{j}室")
##
##


#打印三角形

for i in range(10):
    if i <= 5:
        print("*"*i)
    else:
        print((10-i)*"*")






























