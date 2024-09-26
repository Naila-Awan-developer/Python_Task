class hotal_management_system:
    def __init__(self):
       self.list=[]
       self.status1=False
       self.status2 = True
    def check_in(self):
        user_input=int(input("check the room reserve: "))
        print(user_input)
        if self.list == user_input:
         self.list.append(user_input)
         print(self.list)
        else:
         print("room is reserved")
    def check_out(self):
        user_input =int(input("check the room: "))
        print(user_input)
        # self.list.append(user_input)
        # print(self.list)
        if self.list == user_input:
            del self.list[user_input]
            print(self.list)
        else:
            print("room is not avalible ")
    def stasus(self):
        user_input = int(input("check the room status: "))
        print(user_input)
        if self. list==user_input:
            print( f"{user_input} is availible")
        else:
            print(f"{user_input} is occupie")


# object_H=hotal_management_system()
# object_H.check_in()
# object_H.check_out()
# object_H.stasus()

while True:
    print("1.check_in \n 2.check_out \n 3.status \n 4.for exit program")
    Choice=int(input("enter your choice: "))
    if Choice==1:
        object_H = hotal_management_system()
        object_H.check_in()
    elif Choice==2:
        object_H = hotal_management_system()
        object_H.check_out()
    elif Choice==3:
        object_H = hotal_management_system()
        object_H.stasus()
    else:
        exit()














