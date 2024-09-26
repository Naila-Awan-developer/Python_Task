
def read_int(prompt, min, max):
    try:
        user_input = input("enter a value: ")
        var=int(user_input)
        if var >= -10 and var<= 10:
            print("good value is in range: sa")
        else:
            print("Error: the value is not within permitted range (-10..10)")
    except ValueError:
             print("wrong input,try again:  ")
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
