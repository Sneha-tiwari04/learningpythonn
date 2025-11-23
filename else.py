# write a program to check given number is positive ,negative or zero
num=float(input("enter a number"))
if num>0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number is zero")
    
    #write a program to check grater no amoungs these three numbers
x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
if x>y:
    if x>z:
      print("greter no.is(x):",x)
    else:
        print("greter nomber is (z)",z)
else:
    if y>z:
        print("greter number is (y)",y)
    else:
        print("greter number is (z)",z)