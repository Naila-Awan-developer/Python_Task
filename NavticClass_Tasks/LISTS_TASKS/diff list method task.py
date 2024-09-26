#EXAMPLE:1
a=[5,3,9,6,"ali"]
print(a[-3::])
#EXAMPLE:2
a=[5,3,9,6,"ali"]
print(a[-2::])
#EXAMPLE:3
a=[1,2,3,4,5]
print("here is your list",a)
user=int(input("enter the number:"))
a[-1]=user
print(len(a))
print(a)
del a[1]
print("new a",a)