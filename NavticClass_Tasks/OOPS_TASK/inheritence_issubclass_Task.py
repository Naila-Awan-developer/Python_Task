class Appliance:
    pass
class kitchenAppliance(Appliance):
    pass
class cleaningAppliance(Appliance):
    pass
class Microwave(kitchenAppliance):
    pass
class vacuume(cleaningAppliance):
    pass
for cls1 in [Appliance, kitchenAppliance, cleaningAppliance,Microwave,vacuume]:
    for cls2 in [ Appliance,kitchenAppliance, Microwave,cleaningAppliance]:
        for cls in [Appliance,kitchenAppliance,cleaningAppliance,Microwave,vacuume]:
          print(issubclass(cls1, cls2,), end="\t")
          print()
