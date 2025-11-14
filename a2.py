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
# class grandparent:
#     car="bmw"
#     def home(self):
#          print("home from grandparent")
# class parent:
#     car="icici"
#     def home(self):
#         print("home form parent")
# class child:
#     pass
# obj=child()
# print(obj.car,obj.bank) 
# obj.land()
# obj.home()

# class father:
#     def home(self):
#         print("home from father")
#         mother.home(self)
# class mother:
#     def car(self):
#         print("car from mother")
#     def home(self):
#         print("home from mother")
# class child(father,mother):
#     pass
# obj=child()
# obj.car()
# obj.home()
    
# class parent:
#     def home(self):
#         print("home from parent")
#     def car(self):
#         print("car from parent")
# class chlid1(parent):
#     pass
# class child2(parent):
#     pass
# obj1=chlid1()
# obj2=child2()
# obj1.car()
# obj2.home()

# class parent:
#      def home(self):
#          print("home from parent")
#      def car(self):
#          print("car from parent")
# class child1:
#     def bank(self):
#         print("bank from child1")
# class child2:
#     def land(self):
#         print("land from child2" )
# class child3(parent,child1,child2):
#     pass
# obj1=child3()
# obj1.car()
# obj1.home()
# obj1.bank()
# obj1.land()

# class student:
#     pass
# print(dir(student))

# class student:
#     def add(x,y):
#         print(x+y)
#     def add(x,y,z):
#         print(x+y+z)
#     def add(x,y,z,p):
#         print(x+y+z+p)
# obj=student
# obj.add(10)
# obj.add(10,20)
# obj.add(10,20,30)
# obj.add(10,20,30,40)

from abc import ABC, abstractmethod
class calculater(ABC):
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
            print(a-b)
    def multi(self,a,b):
        print(a+b)
    @abstractmethod
    def div(self):
        pass
class junior(calculater):
    def div(self,a,b):
        print(a/b)
obj=junior()