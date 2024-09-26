def Student_Data():
    f=open("../ data text", "w")
    print(f.write)
    Name = input("enter your name:")
    Father_name = input("enter your Father name:")
    Date_of_birth = input("enter your Date of birth:")
    Gender = input("enter your Gender:")
    age = int(input("enter your age:"))
    email = input("enter your email:")
    phone_num = int(input("enter your phone_num:"))
    Institute_name = input("enter your Education:")
    Subject= input("enter your Subject:")
    f.write(f"name: {Name} '\n' father name:{Father_name} '\n' date of birth:{Date_of_birth} '\n' gender:{Gender} '\n' age:{age} '\n' email:{email} '\n' phone num {phone_num} '\n' institute name:{Institute_name}  '\n' subject:{Subject} ")
    close=("text")
def Retrieve_student_data():
    f=open("../data text", "r")
    print("enter your  name:" )
    print("enter your Father name:")
    print("enter your  Date of birth:")
    print("enter your  Gender:")
    print("enter your  age:")
    print("enter your email:")
    print("enter your phone num:")
    print("enter your Institute name:")
    print("enter your subject:")
    closs=("text")


def course_marks():
    f=open("../data text", "w")
    print(f.write)
    computer=int(input("enter your marks for computer:"))
    english = int(input("enter your marks for english:"))
    maths= int(input("enter your marks for maths:"))
    total=300
    obtained_marks=computer+english+maths
    percentage = (obtained_marks/ total) * 100
    f.write(f"computer:{computer} \n english:{english}\n maths:{maths}\n total:{total}\n obtained:{obtained_marks}\n percentage:{percentage}")
    close=("text")
def Retrieve_course_marks():
    f=open("../marks text", "r")
    print("enter your computer marks:")
    print("enter your english marks:")
    print("enter your maths marks:")
    print("enter total marks:")
    print("enter obtained marks:")
    print("enter your percentage:")
    closs=("text")

print("*"*27)
print("|""Student Information System""|")
print("*"*27)

print('*''!'*7)
print('|Student data|*')
print('*''!'* 7)

print('*''~' * 7)
print('|Course Marks|')
print('*''~' * 7)
while True:
    print("1.student data \n 2.Retrieve student data\n 3.course marks \n 4.Retrieve course data   \n5.for exit program")
    Choice=int(input("enter your choice:"))
    if Choice==1:
       Student_Data()
    elif Choice==2:
        Retrieve_student_data()
    elif Choice==3:
       course_marks()
    elif Choice==4:
        Retrieve_course_marks()

    else:
        exit()

