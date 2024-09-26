print()
print()
print("#"*33)
print("|""DICTIONARY AND DIFFERENT METHODS""|")
print("#"*33)
print()

print()
print("*""^" * 24)
print("|""EXAMPLE OF HINGING INDENT METHOD IN DICTIONARY""|")
print("*""^" * 24)
print()
def Dictionary():
#EXAMPLE:1
    print()
    print("*""~"*16)
    print("|""EXAMPLE OF DICTIONARY AND LIST""|")
    print("*""~"*16)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    words = ['Doll 1', 'Doll 2', 'Doll 3']

    for word in words:
        if word in dictionary:
            print(word, "->", dictionary[word])
        else:
            print(word, "is not in dictionary")

#EXAMPLE:2
# Example 1 hinging method:
dictiyonar = {
              "Name": "Naila",
              "Father Name": "Qasim khan",
              "Roll No": "40"
              }
print(dictiyonar)
# Example 2:
phone_numbers = {'No 1': 5551234567,
                 'No 2': 22657854310
                 }
print(phone_numbers )
def sorted_k_and_unsorted_K ():
#EXAMPLE:3
    print()
    print("*""+"*20)
    print("|""EXAMPLE OF SORTED KEY IN DICTIONARY""|")
    print("*""+"*20)
    print()
    Dictionary = {"Doll 3": "deyana", "Doll 2": "nain", "Doll 1": "laina"}
    print(Dictionary)
    for key in sorted(Dictionary.keys()):
        print(key, "->", Dictionary[key])
#EXAMPLE:4
    print()
    print("*""-"*19)
    print("|""EXAMPLE OF UNSORTED KEY IN DICTIONARY""|")
    print("*""-"*19)
    print()
    Dictionary = {"Doll 3": "deyana", "Doll 2": "nain", "Doll 1": "laina"}
    print(Dictionary)
    for key in Dictionary.keys():
        print(key, "->", Dictionary[key])
def unsorted_v_and_sorted_v():
# EXAMPLE:5
    print()
    print("*""="*20)
    print("|""EXAMPLE OF UNSORTED VALUE IN DICTIONARY""|")
    print("*""=" * 20)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    for french in dictionary.values():
        print(french)
# EXAMPLE:6
    print()
    print("*""!"* 20)
    print("|""EXAMPLE OF SORTED VALUE IN DICTIONARY""|")
    print("*""!"* 20)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    for french in sorted(dictionary.values()):
        print(french)
def item():
# EXAMPLE:7
    print()
    print("*""#" * 15)
    print("|""EXAMPLE OF ITEM IN DICTIONARY""|")
    print("*""#" * 15)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    for english, french in dictionary.items():
        print(english, "->", french)
def adding_v_and_adding_k():
# EXAMPLE:8
    print()
    print("*""$"* 20)
    print("|""EXAMPLE OF ADD NEW VALUE IN DICTIONARY""|")
    print("*""$" * 20)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    dictionary['Doll 1'] = 'lessa'
    print(dictionary)
# EXAMPLE:9
    print()
    print("*" * 38)
    print("|""EXAMPLE OF ADD NEW KEY IN DICTIONARY""|")
    print("*" * 38)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    dictionary['Doll 4'] = 'Aina'
    print(dictionary)
def delete_k():
# EXAMPLE:10
    print()
    print("*""^"* 21)
    print("|""EXAMPLE OF DELETE KEY IN DICTIONARY""|")
    print("*""^"* 21)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    del dictionary['Doll 1']
    print(dictionary)


def popitem_k():
# EXAMPLE:11
    print()
    print("*""-" * 19)
    print("|""EXAMPLE OF POPITEM KEY IN DICTIONARY""|")
    print("*""-" * 19)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    dictionary.popitem()
    print(dictionary)
def update_k():
# EXAMPLE:12
    print()
    print("*""~" * 22)
    print("|""EXAMPLE OF UPDATE METHOD KEY IN DICTIONARY""|")
    print("*""~" * 22)
    print()
    dictionary = {"Doll 1": "laina", "Doll 2": "nain", "Doll 3": "deyana"}
    print(dictionary)
    dictionary.update({"Doll 4": "aina"})
    print(dictionary)
while True:
    print(" 1.Dictionary\n 2.sorted_key_and_unsorted_key \n 3.sorted_value_and_unsorted_value \n 4.item" 
           "\n 5.adding_value_and_adding_key\n 6.delete_key_\n 7.popitem_key\n 8.update_key")
    Choice=int(input("enter your choice:"))
    if Choice==1:
         Dictionary()
    elif Choice==2:
         sorted_k_and_unsorted_K()
    elif Choice == 3:
         unsorted_v_and_sorted_v()
    elif Choice==4:
         item()
    elif Choice==5:
         adding_v_and_adding_k()
    elif Choice==6:
         delete_k()
    elif Choice==7:
         popitem_k()
    elif Choice==8:
         update_k()
    elif Choice == 9:
         'exit_program'
    else:
        exit()