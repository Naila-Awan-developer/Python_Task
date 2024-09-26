#EXAMPLE 1
print()
print("delete one num of the list:")
list=[5,6,7,8,9,]
list1=list
print(list1)
del list1[1]
print(list)
#EXAMPLE 2
print()
print("delete specific part of the  list:")
list=[5,6,7,8,9,]
list1=list
print(list1)
del list1[1:4]
print(list)
#EXAMPLE 3
print()
print("delete specific part of the 2 lists:")
list=[5,6,7,8,9,]
print(list)
list1=list
print(list1)
del list1[1:4]
print(list,list1)

#EXAMPLE4
print()
print("delet and append list")
list=[1,4,6,7,8,9,0]
del list[:]
print(list)
list.append(4)
list.append(10)
list.append(5)
print(list)

#EXAMPLE5
print()
print("empty list ")
list1=[1,4,6,7,8,9,0]
del list1[:]
print(list1)
list2=[6,5,3,4,7,9,]
list1.append(list2)
del list2[:]
print(list1)

print(list2,list1)