def message():
 global x
 x=4
 print("hello",x)
x=3
message()
print(x)
def value():
 global x
 x=6
 print("hello",x)
x=3
value()
print(x)



def my_function(n):
    print("I got", n)
    n += 1
    print("I have", n)


var = 1
my_function(var)
print(var)