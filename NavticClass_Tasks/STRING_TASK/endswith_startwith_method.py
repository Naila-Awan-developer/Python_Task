# startswith_method
text="python programming"
print(text.startswith("py"))
print(text.startswith("pro"))
# 1:
text="python java programming"
print(text.startswith(("py", "java","c")))
# 2:
text="cpython java programming"
print(text.startswith(("py", "java","c")))
# 3:
text="japython java programming"
print(text.startswith(("py", "java","c")))
# 4:
text="javapython java programming"
print(text.startswith(("py", "java","c")))
# 5:
# check index:
text="python programming"
print(text.startswith("python", 7))
print(text.startswith("prog",7))
# 6:
text="PYTHON PROGRAMMING"
print(text.lower().startswith("python"))


text="PYTHON PROGRAMMING"
print(text.lower().startswith("PYTHON"))
