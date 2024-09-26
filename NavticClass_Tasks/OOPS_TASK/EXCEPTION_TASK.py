def fun(num1,num2,operation):

    try:

        if operation=='+':
            return num1+num2
        elif operation=='-':
            return num1-num2
        elif operation=='*':
            return num1*num2
        elif operation=='/':
            return num1/num2
        else:
            raise ValueError("bad input")
    except ValueError:
        print("invalid value")
    except ZeroDivisionError:
        print("bad input...")
    except TypeError:
        print("try agin type error")
while True:
    try:
        num1=float(input("enter your num:"))
        num2 = float(input("enter your num:"))
        operation = input("enter your opertion:")
        fun_v=fun(num1,num2,operation)
        print(fun_v)
    except ValueError:
        print("valeError")
    choice=input("do you want to perform the calculate again use.lower()function ")
    if choice!='yes':
      break
    print("good bye")