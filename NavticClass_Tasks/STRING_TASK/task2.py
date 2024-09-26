file_name=input("Enter you file name: ")
if file_name.startswith("data") or file_name.endswith(".text"):
    print("this is text file:")
elif file_name.startswith("data") or file_name.endswith(".image"):
    print("this is image file:")
elif file_name.startswith("report") or file_name.endswith(".pdf"):
       print("the pdffile:")
else:
    print("the file is not found")

    