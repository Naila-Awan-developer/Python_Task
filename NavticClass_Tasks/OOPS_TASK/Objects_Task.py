# ####### vehicles ########
# class vehicles:
#     def __init__(self,size,color,tyres):
#         self.size=size
#         self.color=color
#         self.tyres=tyres
#     def buying_and_salling(self):
#         print("*** we have available car ***")
#         print("    size of car: ", self.size)
#         print("    color of car: ",self.color)
#         print("    tyres of car: ", self.tyres)
# object_vehicle=vehicles(100,"white",4)
# object_vehicle.buying_and_salling()
#
#
#
#
####### vehicles ########
# class vehicles:
#     size = 100
#     color = 'red'
#     tyres = 4
#     def buying_and_salling(self):
#         print("*** we have available car ***")
#         print("    size of car:", self.size)
#         print("    color of car:",self.color)
#         print("    tyres of car:", self.tyres)
# object_vehicle=vehicles()
# object_vehicle.buying_and_salling()

####### vehicles ########
# class vehicles:
#     def __init__(self):
#        self.size = 100
#        self.color = 'red'
#        self.tyres = 4
#     def buying_and_salling(self):
#         print("*** we have available car ***")
#         print("    size of car:", self.size)
#         print("    color of car:",self.color)
#         print("    tyres of car:",self.tyres)
# object_vehicle=vehicles()
# object_vehicle.buying_and_salling()

###### vehicles ########
class vehicles:
    def __init__(self):
       self.make = 'HOnda'
       self.model = 1999
       self.year =2001
       self.color='green'
       self.is_running=False
    def start_engien(self):
        if not self.is_running:
            self.is_running=True
            print(f"The{self.year} {self.make}{self.model} engine is now running.")
        else:
            print(f"The{self.year} {self.make}{self.model} engine is already running of.")

    def honk(self):
        print(f"The{self.color} {self.make}{self.model} goes 'Beep Beep!'.")

    def display_info(self):
        print("")
object_vehicle=vehicles()
object_vehicle.start_engien()
object_vehicle.honk()
object_vehicle.display_info()



































