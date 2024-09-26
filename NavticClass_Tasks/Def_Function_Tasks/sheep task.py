def sheep_complete():
    print("your sheep is complete\n take a shower")
def search_sheep():
        print("your sheep is missing \n search a sheep")
def  sleep_and_dream():
          print("need sleep and happy dream")
def feed():
    print("feed the sheep dog")

sheeps=int(input("enter the number of sheep:"))
if sheeps>=120:
    sheep_complete()
elif sheeps<=120:
 search_sheep()
elif sheeps>=120:
 sleep_and_dream()
else:
    exit()
feed()