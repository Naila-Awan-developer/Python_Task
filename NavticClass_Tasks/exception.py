def bad_fun():
    val1 = input("Enter your first value ")
    val2 = input("Enter your second value ")


    if val2 == 0:
        print("the second value could not be.o")
        raise ZeroDivisionError("the second value is 0.")
    elif val1<0 or val2<0:
        raise ValueError("string value cannot be added")
    else:
        result=val1/val2
        print("the result is:"result)
    try:
        bad_fun()
    except ArithmeticError:
        print("What happened? An error?")
    except ValueError:
        print("What happened? An error?")

print("THE END.")
