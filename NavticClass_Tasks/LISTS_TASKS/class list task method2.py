def insert(list1):

    i = 0
    while i <= 5:
        list1.insert(i, i + 1)
        i += 1
        print(list1)


def append(list2):
      # creating an empty list
    i = 0
    while 1 <= 5:
        list2.append(i+1)
        i += 1
        print(list2)
list1=[]
list2=[]
print("insert fun data", insert(list1))
print("append fun data", append(list2))

