var1=input("Enter your word:")
var2=input("Enter your word:")
var1=var1.replace('','').lower()
var2=var2.replace('','').lower()
var1_s=sorted(var1)
# print(var1_s)
var2_s=sorted(var2)
# print(var1_s)
if var1==var2:
    print("the word is anagram")
else:
    print("the word is not anagram")