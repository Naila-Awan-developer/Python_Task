#rFIND() METHOD
takepath=input("Enter your path:")
def filepath(path):
    variable=path.rfind("/")
    if variable!=-1:
        foundpath=path[variable+1:]
    else:
        foundpath=path
    if not foundpath:
        return "file not found"
    return foundpath
function=filepath(takepath)
print(function)