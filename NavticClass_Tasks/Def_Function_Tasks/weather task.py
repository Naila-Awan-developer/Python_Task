def go_for_walk():
    print("the weather is good go for a walk")
def have_lunch():
    print("and lunch yes")
def stay_home():
    print("the weather is bad stay home")
user=(input("enter about the weather good or bad:"))
if user=='good':
  go_for_walk()
  have_lunch()
elif user=='bad':
    stay_home()

else:
    exit()


