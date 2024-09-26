def mysplit(string):
    list=[]
    variable=''
    for ch in string:
        if ch=='':
          if variable:
            list.append(variable)
            variable=''
        else:
           variable+=ch

    if variable:
        list.append(variable)
        return list


# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))
string=input("Enter your string: ")
print(mysplit(string))



















