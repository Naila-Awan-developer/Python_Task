class Device:
    pass
class PortalDevice(Device):
    pass
class WiredDevice(Device):
    pass
class SmartPhone(PortalDevice):
    pass
class DesktopComputer(WiredDevice):
    pass

obj1 = Device()
obj2 = PortalDevice()
obj3 = WiredDevice()
obj4 = SmartPhone()
obj5 = DesktopComputer()

for obj in [obj1, obj2, obj3,obj4,obj5]:
    for cls in [Device, PortalDevice, WiredDevice,SmartPhone,DesktopComputer]:
        print(isinstance(obj, cls), end="\t")
    print()
