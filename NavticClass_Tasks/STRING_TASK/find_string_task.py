# FIND METHOD TASK:
var1=input("enter yor sentence:")
var2=input("enter your word:")
result=(var1.find(var2))
if  result!=-1:
    print(f"the  var1 '{var1}' found at position '{result}'")

else:
    print(f"the var1 '{var1}'  not found")

# method 2:
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

# method  3:
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
