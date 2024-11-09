# class star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#
#     def __str__(self):
#         return self.name + ' in ' + self.galaxy
#
# sun = star('Sun', 'the Milky Way')
# print(sun)
#
# class planet:
#     def __init__(self, name, star):
#         self.name = name
#         self.star = star
#
#     def __str__(self):
#         return self.name + ' orbits ' + self.star.name + ' in ' + self.star.galaxy
#
# planetobj = planet('Earth', sun)
# print(planetobj)

##################Tables

# for i in range(1,11):
#     for j in range(1,11):
#         print(i ,'*',j,'=', i*j)


##################practice   issubclass
# class Appliance:
#     def __init__(self):
#         pass
#
# class KitchenAppliance(Appliance):
#     def __init__(self):
#        Appliance().__init__()
#
# class Microwave(KitchenAppliance):
#             def __init__(self):
#                 KitchenAppliance().__init__()
#
#
#
# class CleaningAppliance(Appliance):
#     def __init__(self):
#         Appliance().__init__()
# class Vacuum(CleaningAppliance):
#             def __init__(self):
#                 CleaningAppliance().__init__()
#                 pass
#
#
#
# for cls1 in [Appliance, KitchenAppliance, CleaningAppliance,Microwave,Vacuum]:
#     for cls2 in [Appliance, KitchenAppliance, CleaningAppliance,Microwave,Vacuum]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()

################# practice of isinstance

# class Device:
#     pass
#
#
# class PortalDevice(Device):
#     pass
#
#
# class WiredDevice(Device):
#     pass
#
#
# class SmartPhone(PortalDevice):
#     pass
# class DesktopComputer(WiredDevice):
#     pass
#
#
# obj1 = SmartPhone()
# obj2 = DesktopComputer()
# obj3 = Device()
# obj4=WiredDevice()
# obj5=PortalDevice
#
# for obj in [obj1,obj2,obj3,obj4,obj5]:
#     for cls in [SmartPhone,DesktopComputer,Device,WiredDevice,PortalDevice]:
#         print(isinstance(obj, cls), end="\t")
#     print()


##############practic of classes

# class grandparent():
#     pass
# class parent(grandparent):
#     pass
# class children(parent,grandparent):
#     pass
# class grandchildren(children,parent,grandparent):
#     pass
#
# for i in [grandchildren,parent,children,grandparent]:
#     for j in [grandchildren,parent,children,grandparent]:
#         print(isinstance(i,j), end='\t')
#     print()
#
# for i in [grandchildren,parent,children,grandparent]:
#     for j in [grandchildren,parent,children,grandparent]:
#         print(isinstance(i,j), end='\t')
#     print()

###################
# class grandparent:
#     def __init__(self):
#         self.var = 101  # Make var an instance attribute by using self.
#
#
# class parent(grandparent):
#     def __init__(self, status1=None):
#         super().__init__()  # Properly call the parent class constructor
#         self.status1 = status1  # Initialize status1
#
# class children(parent):
#     def __init__(self, status1=None, status2=None):
#         super().__init__(status1)  # Initialize status1 from the parent class
#         self.status2 = status2  # Initialize status2
#
# # Create an object of children and pass values for status1 and status2
# obj = children(status1="Active", status2="Learning")
#
# # Access the attributes
# print(obj.status1)
# print(obj.status2)



########### multiple inheritance
# Multiple Inheritance Example

# class Father:
#     def height(self):
#         return "6 feet"
#
# class Mother:
#     def eye_color(self):
#         return "brown"
#
# # Child class inherits from both Father and Mother
# class Child(Father, Mother):
#     pass
#
# # Creating an object of Child class
# child_obj = Child()
#
# print("Height:", child_obj.height())   # Inherited from Father
# print("Eye Color:", child_obj.eye_color())  # Inherited from Mother

############multi level inheritance


# Multilevel Inheritance Example

# class Grandparent:
#     def family_name(self):
#         return "Smith"
#
# class Parent(Grandparent):
#     def profession(self):
#         return "Engineer"
#
# # Child class inherits from Parent, which in turn inherits from Grandparent
# class Child(Parent):
#     def hobby(self):
#         return "Painting"
#
# # Creating an object of Child class
# child_obj = Child()
#
# print("Family Name:", child_obj.family_name())  # Inherited from Grandparent
# print("Profession:", child_obj.profession())    # Inherited from Parent
# print("Hobby:", child_obj.hobby())              # Defined in Child class






