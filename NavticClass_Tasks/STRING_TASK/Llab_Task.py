
def fun(user_input ,shift):
    encrypted_text=''
    shift=shift % 26
    for char in user_input:
        if char.isalpha():
            if char.islower():
                base=ord('a')
            else:
                base = ord('A')
                new_char = chr((ord(char) - base + shift) % 26 + base)
                encrypted_text += new_char
        else:
            encrypted_text += char
        return encrypted_text

    user_input = input("Enter your valve")
    while True:
        try:
            encrypt=input("Enter a line of text to encryption: ")
            shift=int(user_input)
            if shift<=1:
                print(shift)
            elif shift>=25:
                print(shift)
            else:
                print("Enter a valid number")
                break
        except ValueError:
            print("invalid input please enter the integer again")

function=fun()
print(function)
# the task is uncomplete










