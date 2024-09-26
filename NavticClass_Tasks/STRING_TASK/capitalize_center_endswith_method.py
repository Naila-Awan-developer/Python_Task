#EXAMPLE OF DIFFERENT METHOD:
# Demonstrating the capitalize() method:
# 1:
a='aBcD'
print(a.capitalize())
# 2:
print('aBcD'.capitalize())
# 3:
print("Alpha".capitalize())
# 4:
print('ALPHA'.capitalize())
# 5:
print(' Alpha'.capitalize())
# 6:
print('123'.capitalize())
# 7:
print("αβγδ".capitalize())
print()
#CENTER () METHOD:
# Demonstrating the center() method:
# 1:
print('[' + 'alpha'.center(10) + ']')# 5 alpha nai lai le space tu 5 rehgaya tu kam wala start mai ayega or or zyada last mai yane 2 start mai or 3 last main:
print('[' + 'alpha'.center(10,"*") + ']')
# 2:
print('[' + 'Beta'.center(2) + ']')#no padding kio kai string ka length zyada hai or padding ka kam:
# 3:
print('[' + 'Beta'.center(4) + ']')
# 4:
print('[' + 'Beta'.center(6) + ']')
# 5:
print('[' + 'gamma'.center(20, '*') + ']')

# endswith():
# Demonstrating the endswith() method:
# 1:
if "epsilon".endswith("on"):
    print("yes, it end with on")
else:
    print("no, it does not end with on")

# 2:
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))