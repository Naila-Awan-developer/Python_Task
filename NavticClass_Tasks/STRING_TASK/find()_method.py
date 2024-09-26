# FIND ():
# Demonstrating the find() method:
# 1:
print("Eta".find("ta"))# find method show the index of first word:and error ke jaga -1 show huga
print("Eta".find("mma"))
# 2:
t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
# 3:
print('kappa'.find('a', 2))

# method 4:
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


# method 5:
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))