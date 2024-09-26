c0=int(input("enter the num: "))
steps=0
while c0>0:
    if c0%2==0:
        c0=c0%2
        print("c0")
    elif c0%2!=0:
        c0=3*c0+1
        print("c0")
    else:

        c0 = 3 * c0 + 1
print("c0")
steps+=steps
print(steps)