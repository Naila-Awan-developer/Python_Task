list1=[3,4,6,8,9,5,6,2,1,]
print("orignal list",list1)
list2=list1[:]
print("(:) full list",list2)
list3=list1[2:6]
print("(2:6) copy 4 num of the list",list3)
list4=list1[1::4]
print("(1::4) copy  of list 2 fix  num:",list4)
list5=list1[2::]
print("(2::) copy start index num into last num of the list",list5)
list6=list1[:7]
print("(:7)copy start num of the list into fix  index num",list6)
list7=list1[3:]
print("(3:)copy 8 to last num of the list",list7)