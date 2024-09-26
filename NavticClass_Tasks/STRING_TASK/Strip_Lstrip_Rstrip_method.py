# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")
print("["+    "cisco.com ".strip().replace("sc","")+"]")
print("["+    "cisco.com ".strip().replace("com","")+"]")
print("["+    "cisco.com ".strip().replace("c","")+"]")
print("["+    "cisco.com ".strip().replace(".com","")+"]")
print("["+    "cisco.com ".strip().replace("com","")+"]")
print("["+    "cisco.com ".strip().replace("c","r",2)+"]")
text="   Hello world!  "
print(text.strip())
text="*****Hello world!****"
print(text.strip())

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))
print("www.cisco.com".lstrip(".com"))
print("www.cisco.com".lstrip("com"))
text="   Hello world!  "
print(text.lstrip())
text="*****Hello world!"
print(text.lstrip())
print("["+"     Hello world!  " .lstrip()+"]")


# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))
print("cisco.com".rstrip(".moc"))
print("cisco.com".rstrip("moc"))
print("cisco.com".rstrip("com"))
print("cisco.com".rstrip(".com"))
print("["+    "cisco.com ".rstrip().replace("com","w",2)+"]")
print("["+   "callibri cisco com ".rstrip().replace("c","")+"]")
print("["+ "cisco.com".rstrip("c")+"]")