# Testing properties: class variables.
class Super:
    supVar = 1
class Sub(Super):
    subVar = 2
obj = Sub()

print(obj.subVar)
print(obj.supVar)


# Testing properties: instance variables.
class Super:
    def __init__(self):
        self.supVar = 11
class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12
obj = Sub()
print(obj.subVar)
print(obj.supVar)
