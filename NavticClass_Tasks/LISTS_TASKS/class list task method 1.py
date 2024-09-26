l1=[1,2,3,4,5] #CREATE LIST1
l2=[6,7,8,9,10] #CREATE LIST 2
print("original list",l1, l2) # PRINT LIST 1 AND 2
l1[1]=l2[1] #REPLACE LIST 2 VALUE(7) WITH LIST 1 VALUE(2)
print(" replace list ",l1,l2) # PRINT REPLACE VALUE LIAT 1 AND LIST 2
l1[2]=l2[3] #COPY LIST 2 VALUE(9) WITH LIST 1 VALUE(3)
print("copy list",l1,l2) # PRINT REPLACE VALUE LIAT 1 AND LIST 2
del l1[1]
print("delet list",l1)
l1.insert(1,"jawad")
print("insert list",l1)


#TASK2
def insert():
    insert_list = []
    i=0
    while i<=5:
        insert_list.insert(i, i + 1)
        i+=1
    print(insert_list)


def append():
    append_list = []  # creating an empty list
    i=0
    while i<=5:
        append_list.append( i + 1)
        i+=1
    print(append_list)


print("insert function data",insert())
print("append function data", append())



