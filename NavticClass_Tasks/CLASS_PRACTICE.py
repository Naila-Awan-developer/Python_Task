# # # def addition():
# # #     name="naila"
# # #     print(name)
# # #
# # # addition=2
# # # # print(addition)
# # # bolstatus=True
# # # if bolstatus:
# # #     print("bulb is on")
# # # else:
# # # status=(input("satus 1,0"))
# # # if status==1:
# # #     print("on")
# # # elif status!=1:
# # #      print("of")
# # # else:
# # #         exit()
# #
# # def Student_Data():
# #     f=open(" data text","w")
# #     print(f.write)
# #     Name = input("enter your name:")
# #     Father_name = input("enter your Father name:")
# #     Date_of_birth = input("enter your Date of birth:")
# #     Gender = input("enter your Gender:")
# #     age = int(input("enter your age:"))
# #     email = input("enter your email:")
# #     phone_num = int(input("enter your phone_num:"))
# #     Institute_name = input("enter your Education:")
# #     Subject= input("enter your Subject:")
# #     f.write(f"name: {Name} '\n' father name:{Father_name} '\n' date of birth:{Date_of_birth} '\n' gender:{Gender} '\n' age:{age} '\n' email:{email} '\n' phone num {phone_num} '\n' institute name:{Institute_name}  '\n' subject:{Subject} ")
# #     close=("text")
# # def course_marks():
# #     f=open("marks text","w")
# #     print(f.write)
# #     computer=int(input("enter your marks for computer:"))
# #     english = int(input("enter your marks for english:"))
# #     maths= int(input("enter your marks for maths:"))
# #     total=300
# #     obtained_marks=computer+english+maths
# #     percentage = (obtained_marks/ total) * 100
# #     f.write(f"computer:{computer} \n english:{english}\n maths:{maths}\n total:{total}\n obtained:{obtained_marks}\n percentage:{percentage}")
# #     close=("text")
# # def Retrieve_course_marks():
# #     f=open("marks text","r")
# #     print("enter your  name:")
# #     print("enter your Father name:")
# #     print("enter your  Date of birth:")
# #     print("enter your  Gender:")
# #     print("enter your  age:")
# #     print("enter your email:")
# #     print("enter your phone num:")
# #     print("enter your Institute name:")
# #     print("enter your subject:")
# #     print("enter your computer marks:")
# #     print("enter your english marks:")
# #     print("enter your maths marks:")
# #     print("enter total marks:")
# #     print("enter obtained marks:")
# #     print("enter your percentage:")
# #     closs=("text")
# #
# # print("*"*27)
# # print("|""Student Information System""|")
# # print("*"*27)
# #
# # print('*'*20)
# # print('|Student data|*')
# # print('*'*20)
# #
# # print('*' * 20)
# # print('|Course Marks|')
# # print('*' * 20)
# # while True:
# #     print("1.student data \n 2.course marks \n 3.Retrieve course data   \n4.for exit program")
# #     Choice=int(input("enter your choice"))
# #     if Choice==1:
# #        Student_Data()
# #     elif Choice==2:
# #        course_marks()
# #     elif Choice==3:
# #         Retrieve_course_marks()
# #     else:
# #
# #         exit
# import cv2
# thres = 0.5 # Threshold to detect object
#
# cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(10,70)
#
# classNames= []
# classFile = 'coco.names'
# with open(classFile,'rt') as f:
#      classNames = f.read().rstrip('\n').split('\n')
#
# configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
# weightsPath = 'frozen_inference_graph.pb'
#
# net = 'cv2.dnn_DetectionModel(weightsPath,configPath)'
# 'net.setInputSize(320,320)'
# 'net.setInputScale(1.0/ 127.5)'
# 'net.setInputMean((127.5, 127.5, 127.5))'
# 'net.setInputSwapRB(True)'
#
# while True:
#     success,img = cap.read()
#     classIds, confs, bbox = net.detect(img,confThreshold=thres)
#     print(classIds,bbox)
#
#     if len(classIds) != 0:
#         for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
#             cv2.rectangle(img,box,color=(0,255,0),thickness=2)
#             cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
#             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#             cv2.putText(img,str(round(confidence*100,2)),(box[0]+200,box[1]+30),
#             cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
#
#     cv2.imshow("Output",img)
#     cv2.waitKey(1)
import random
#import example value change the name of thi method is supper seed:
# from math import pi
# result=pi
# print(result)
# pi=2.4
# print(pi)

# pi = 3.14
#
#
# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None
#
#
# print(sin(pi / 2))
#
# from math import sin, pi
#
# print(sin(pi / 2))


# import math
#
# for name in dir(math):
#     print(name, end="\t")
# import sys
# lsit=[]
# while i<=20:
#     list.append
#
# the code is un complete


#POINT 1: lenth checking for user input:
user=input("enter your string:")
length=len(user)
if length%2==0:
    print("even string")
    print()
else:
    print("odd string")
    print(length)
user+= ""
length+=1
print(":",length)

#POINT 2: character Analysis:
max_char=user
min_char=user
print("max:",max(max_char))
print("min:",min(min_char))

#POINT 3:string manipulation:
if length%2!=0:
    user+=""

#POINT 4: slicing
half_index=length//2
first_half=user[:half_index]
second_half=user[half_index:]
print("first_half:",first_half)
print("second_half:", second_half)

 #POINT 5:string index:
try:
   index=user.index('a')
   print("index of'a':",index)
except ValueError:
   print("a' is not in the string")

# point 6: design:
print('*''+'*10)
print("*{the task is over}*")
print('*''+'*10)
# main="""{a}
#         {b}
#         {c}"""
# print(main)






