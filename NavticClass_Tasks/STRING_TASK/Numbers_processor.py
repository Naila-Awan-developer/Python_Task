# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
print("the list become as: ",strings)
total = 0
try:
    for substr in strings:
        total += float(substr)# total=0+2, total=2+3
    print("The total is:", total)
except:
    print(substr, "is not a number.")





#OutPut
#