## Function ##
def add(num1,num2):
    return num1+num2
result=add(5,3)
print(result)

## methods ##
class Calculator:
    def add(self,num1, num2):
        return num1 + num2

obj=Calculator()
result = obj.add(5, 3)
print(result)


### Class  ###
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
         self.balance+=amount

    def withdraw(self, amount):
        self.balance-= amount

account=BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print(account.balance)

#### car #####
class car:
    def __init__(self,brand,model):
        self.brand=brand # Attribute (data)
        self.model=model
    def start_engine(self):
        print(f"{self.brand},{self.model}'s engine started.")#Method (behaviour
#Creating object (instaance of the class car)
my_car=car("toyota","corola")
my_car.start_engine()


######
class car:
    def __init__(self,name,capacity):
        self.name=name # Attribute (data)
        self.capacity=capacity

    def move(self):
        return f"{self.name} is moving on."
    def description(self):
        return f"{self.name} is a vehicle with {self.capacity}"
####3# uncomplete code




class Animal:
   pass
class Mammal:
    pass
class bird:
    pass
class Sub(Mammal, bird):
        pass

def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')


printBases(Mammal)
printBases(bird)
printBases(Sub)

