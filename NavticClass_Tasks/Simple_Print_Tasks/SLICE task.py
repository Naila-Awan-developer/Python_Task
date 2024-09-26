# Copying the entire list.
list_1 = [1,4,7,5,9,8]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]#3ke value print nahi huge 2 tak huge
print(new_list)


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:5:2]# use rang fun
print(new_list)


my_list = [10, 8, 6, 4, 2]
new_list = my_list[1::4]#3ke value print nahi huge 2 tak huge
print(new_list)