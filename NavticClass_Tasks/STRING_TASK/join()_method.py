# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))
# Demonstrating the lower() method:
print("SiGmA=60".lower())
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
#2:
print("www.cisco.com".lstrip("w."))
# 3:
print("pythoninstitute.org".lstrip(".org"))
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
#2:
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demonstrating the split() method:
print("phi       chi\npsi".split())

# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")

# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())

print()

# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())

print()

# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())

#######
# def mysplit(strng):
#
#
# #
# # put your code here
# #
#
#
# print(mysplit("To be or not to be, that is the question"))
# print(mysplit("To be or not to be,that is the question"))
# print(mysplit("   "))
# print(mysplit(" abc "))
# print(mysplit(""))