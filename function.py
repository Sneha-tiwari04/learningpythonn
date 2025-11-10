# def display():
#     return "hello"
# display()
# print(display())
# res=display()

# def display(n):
#     for i in range(1,n+1):
#         print(i)
# n=int(input("enter how many number:"))
# display(n)

# def display(n):
#     for i in range(1,n+1):
#         print(2*i)
# n=int(input("enter how many number:"))
# display(n)

# def display(n):
#     for i in range(1,n+1,2):
#         print(i)
# n=int(input("enter how many number:"))
# display(n)

# def display(n):
#     for i in range(1,n+1):
#         print(2*1-n)
# n=int(input("enter how many number:"))
# display(n)

# def display(n):
#     for i in range(1,n+1):
#         print(i)
# n=int(input("enter how many number:"))
# display(n)

# def add(z,x,y):
#     print(x,y,z)
#     pass
# add(10,20,30)

# def addd(*args):
#     print(args)
#     print(type(args))
# add(10,20,30,"python",5)

# def add(*n):
#     sum=0
#     for i in n:
#         sum=sum+1
#     print("sum=",sum)
# add(10)
    
# def add(*n):
#     print(n)
#     print(type(n))
# x=eval(input("enter tuble value"))
# add(x)
# add(1,2,3,4,5)

# x=(10)
# y=10
# print(type(x),print(type(y)))

# p=10,
# print(type(p))

# x=1,2,3,4,5
# print(type(x))


# def add(*n):
#     sum=0
#     for i in n:

#             sum=sum+i
#     print("sum:",sum)
# x=eval(input("enter any tuble value"))
# add(*x)

# def add(x,y=0,*z):
#     print(x)
#     print(y)
#     print(z)
#add(1,2,3,4,5,6,7,9,8,10)
    
# key-woard position argu.
# def funname(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# funname(y=20,z=40,x=50)

#5.defult key-word
# def funname(x,y,z):
#     print(x)
#     print(y)
#     print(z)
# funname(y=20,z=40,x=50)

# def funname(**kwargs)

# def display(**n):
#     print(n)
#     print(type(n))
# x=eval(input("enter key-word value:"))
# display(**x)

# def display(**n):
#      print(n)
#      print(type(n))
# x=eval(input("enter key-word value:"))
# display(**x)

# def display():
#     return "welcome"
# x=eval(input("enter a number:"))
# print()

x=10
def show():
    print(x)
show()
print(x)

x=10
def show():
    x=20
    print(x)
show()
print(x)

x=10
def show():
    global x
    x=20
    print(x)
print()
show()
print(x)

x=20
def show():
    print(globals()['x'])
    x=10
show()
