# class parent:
#     city='Bhopal'
#     def car(self):
#         print("car from parent")
# class child (parent):
#     pass
# obj=child()
# print(obj.car)
# obj.car()

#single level 
# class parent:
#     car="bmw"
#     def home(self):
#         print("home from parent")
# class child(parent):
#     car="altro"
#     car2=parent.car
#     def home(self):
#         super().home()
#         print("home from child")
# obj=child()
# print(obj.car)
# print(obj.car2)
# obj.home()

#malti level 
class grandparent:
    car="bmw"
    def home(self):
         print("home from grandparent")
class parent:
    car="icici"
    def home(self):
        print("home form parent")
class child:
    pass
obj=child()
print(obj.car,obj.bank) 
obj.land()
obj.home()