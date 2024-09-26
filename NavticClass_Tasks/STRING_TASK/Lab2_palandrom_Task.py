var1=input("Enter your massege: ")
var1.replace('','').islower()
if  var1=='':
    print("the massege is not paindrom")
else:
   if var1==var1.index[:,-1]:
       print("the massege is palindrom")
   else:
       print("the is not paindrom")
       