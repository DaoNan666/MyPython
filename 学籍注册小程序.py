#  1. 数据存到文件里的格式


#  2. 实现手机号，身份证号在文件里同样数据只有一条,可将文件里的手机号身份证号两项加载到
#      内存，以列表形式存放，用户一输入相关列，就到列表检查是否重复

#  3.选学科时，给用户列出来选项。供选择

db_file = "student_data.db"


# 优化：手机号优化
def phone_info(num):
    if not num.isdigit():
        exit("手机号必须是数字")
    if len(num) != 11:
        exit("手机号必须达到11位")


def register_api():
    stu_data = {}  # 存放学生信息
    print("欢迎报考我们学校".center(50, "-"))
    print("请完成学籍注册")
    name = input("姓名：").strip()
    age = input("年龄：").strip()
    phone = input("电话：").strip()
    if phone in phone_list:
        exit("该手机号已注册")
    phone_info(phone)
    id_num = input("身份证号：").strip()
    if id_num in id_num_list:
        exit("该身份证号已注册")

    course_list = ["c语言", "java", "操作系统", "数据库", "数据结构", "大数据与云计算"]
    for index, course in enumerate(course_list):
        print(f"{index}.{course}")

    select_course = input("请选课：")
    if select_course.isdigit():
        select_course = int(select_course)
        if 0 <= select_course < len(course_list):  # 在序号里选课
            picked_course = course_list[select_course]
        else:
            exit("不合法选项")
    else:
        exit("非法输入")
    stu_data["name"] = name
    stu_data["age"] = age
    stu_data["phone"] = phone
    stu_data["id_num"] = id_num
    stu_data["course"] = picked_course

    return stu_data


# 将学生信息存到文件里
def commit_to_db(filename, stu_data):
    f = open(filename, "a")
    row = f"{stu_data['name']},{stu_data['age']},{stu_data['phone']},{stu_data['id_num']},{stu_data['course']}\n"
    f.write(row)
    f.close()


def load_data(filename):
    f = open(filename)
    phone_list = []
    id_num_list = []
    for line in f:
        line = line.split(",")
        phone = line[2]
        id_num = line[3]
        phone_list.append(phone)
        id_num_list.append(id_num)

        return phone_list, id_num_list


phone_list, id_num_list = load_data(db_file)

student_data = register_api()

print(student_data)

commit_to_db(db_file, student_data)
