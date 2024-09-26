print("*"*20)
print("|""EXAMPLE OF TOUPLES""|")
print("*"*20)
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)

 #EXAMPLE 2
print()
print("*"*35)
print("|""EXAMPLE OF TOUPLES ADD NEW VALUE ""|")
print("*"*35)
my_tuple = (1, 10, 100)
print(my_tuple)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)

#EXAMPLE:3
print()
print("*"*35)
print("|""EXAMPLE OF TOUPLES ADD NEW VALUE ""|")
print("*"*35)
my_tuple = (1, 10, 100)
print(my_tuple)
t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1[3])
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)


print()
print("*"*30)
print("|""EXAMPLE OF  SWAPPING TOUPLES  ""|")
print("*"*30)
var = 123
print(123)
t1 = (1, )
t2 = (2, )
t3 = (3, var)
print("before swapping")
print("t1",t1,"t2",t2,"t3",t3)
t1, t2, t3 = t2, t3, t1
print("after swapping")
print("t1",t1,"t2", t2,"t3", t3)
