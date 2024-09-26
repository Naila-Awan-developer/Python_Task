def Student_Data():

    Name = input("enter your name:")
    Father_name = input("enter your Father name:")
    Date_of_birth = input("enter your Date of birth:")
    Gender = input("enter your Gender:")
    age = int(input("enter your age:"))
    email = input("enter your email:")
    phone_num = int(input("enter your phone_num:"))
    Institute_name = input("enter your Education:")
    Class= input("enter your class:")
    Roll_No= int(input("enter your Roll no: "))


    print("enter your  name", Name)
    print("enter your Father name", Father_name)
    print("enter your  Date of birth", Date_of_birth)
    print("enter your  Gender", Gender)
    print("enter your  age", age)
    print("enter your email", email)
    print("enter your phone num", phone_num)
    print("enter your Institute name", Institute_name)
    print("enter your Clss", Class)
    print("enter your  Roll num", Roll_No)

def course_marks():
    computer=int(input("enter your marks for computer:"))
    english = int(input("enter your marks for english:"))
    maths= int(input("enter your marks for maths:"))
    total=300
    obtained_marks=computer+english+maths
    percentage = (obtained_marks/ total) * 100
    print("enter your percentage is",{percentage})
    if percentage>=80:
        print("congrates you got A grade and percentage is ",{percentage})
    elif percentage>=70:
        print("congrates you got B grade and percentage is",{percentage})
    elif percentage>=60:
        print("Good you got C grade and persentage is ",{percentage})
    elif percentage>=50:
        print("congrates you got D grade and percentage is",{percentage})
print("you are fail")
print("#","*"*25,"#")
print("|""Student Information System""|")
print("#""*"*27)
while True:
    print("1.student data \n 2.course marks \n 3.grade \n 4.for exit program")
    Choice=int(input("enter your choice"))
    if Choice==1:
       Student_Data()
    elif Choice==2:
       course_marks()
    elif Choice==3:
         'grade'
    else:
        exit()

