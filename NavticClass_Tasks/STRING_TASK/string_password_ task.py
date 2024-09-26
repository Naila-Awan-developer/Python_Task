# USING ENDSWITH AND CAPITALIZE AND CENTER METHOD:
# user=input("enter your password:")
# if user.endswith("ion"):
#     print("your password is correct")
#     print(user .capitalize())
#     print( '[' + user.center(15) +']')
# else:
#     print("it does not correct your password")



# user=input("Enter your sentence:")
# if user.endswith("?"):
#     print("This is a question")
# elif user.endswith("!"):
#     print("this is  a order")
# else:
#     print("it is improper sentence:")



user=input("Enter your file name:")
if user.endswith("data.pdf"):
    print("uploading pdf file:")
elif user.endswith("data.text"):
    print("uploading text file:")
elif user.endswith("data.jpeg"):
    print("uploading jpeg file:")
elif user.endswith("image.png"):
    print("uploading image.png  file:")
else:
    print("invalid file:")