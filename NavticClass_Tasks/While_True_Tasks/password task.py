password ="python Rocks"
Max_attempts = 5
attempt=0
while attempt<Max_attempts:
    print("enter the password")
    guess=(input("enter the passwod"))
    if guess==password:
      print("congratulation ! you've guess the password")
      break
    # else:
      #    attempt=5
      # if attempt<Max_attempts:




