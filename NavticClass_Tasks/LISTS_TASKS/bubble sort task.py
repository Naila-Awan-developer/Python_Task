def bubble_sort(list):
    noofpass=len(list)
    for i in range(noofpass-1):
        for j in range(noofpass-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list=[8,10,6,2,4]

#EXAMPLE2
my_list = [8, 10, 6, 2, 4]  # list to sort
swapped = True  # It's a little fake, we need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print(my_list)

#EXAMPLE2
list=[]
print(list)
list.sort()
print(list)
#EXAMPLE3
list=[]
print(list)
list.sort()
print(list)
