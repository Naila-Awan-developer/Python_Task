# Demonstrating the split() method:
# 1:
print("phi       chi\npsi".split())
# 2:
text="apple orange banana grape"
split_list=text.split()
print(split_list)
# 3:
text="apple orange banana grape"
split_list=text.split(",")
print(split_list)
# 4:
text="apple-orange-banana-grape"
split_list=text.split("-",2)
print(split_list)
# 5:
text=""" Line1
Line2
Line3"""
split_list=text.split("\n")
print(split_list)
# re.split_method
import re
text="apple;orange,banana_graph"
split_list=re.split(r'[;,_]',text)
print(split_list)

text="apple;orange,banana_graph@pineapple"
split_list=re.split(r'[;,_@]',text)
print(split_list)
#rsplit_method:


text="apple-orange-banana-grape"
split_list=text.rsplit("-",2)
print(split_list)