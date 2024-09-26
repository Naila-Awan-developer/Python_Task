#EXAMPLE:1
print()
print("function calling:")
print()
def my_function():
    a1 = int(input("enter your  first value:"))
    a2 = int(input("enter your  first value:"))
    sum = a1 + a2
    print("the result is:", sum)
my_function()


#EXAMPLE:2
print()
print("calling function:")
print()
def message():
    print("Enter a value: ")

message()
a = int(input())
message()
b = int(input())
message()
c = int(input())


#EXAMPLE:3 #parameter function
print()
print("simple parameter and  aurgument:")
print()
def fun(a1): #parameter
    print("a1:",a1)

fun(5) #argument

#EXAMPLE:4
print()
print("parameter and aurgument:")
print()
def message(number):
    print("Enter a number:", number)
number=6
message(1)
print(number)



#EXAMPLE:5 #positional parameter
print()
print("positional parameter:")
print()
def message(what, number):
    print("Enter", what, "number", number)

message("telephone", 11)
message("price", 5)
message("number", "number")


#EXAMPLE:6 #keyword aurgument:
print()
print("keyword aurgument:")
print()
def introduction(first_name, last_name):
    print("Hello, my name is", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


#EXAMPLE:7
print()
print("mix parameter and aurgument:")
print()
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Call the adding function here.
adding(2,5,6)

#EXAMPLE:8
print()
print("by default value parameter and aurgument:")
print()
def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.
introduction("James")


#EXAMPLE:9
print()
print("by default value parameter without aurgument:")
print()
def introduction(first_name="james", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.
introduction()