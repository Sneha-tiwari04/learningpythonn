# write a program to check given number is positive ,negative or zero
'''num=float(input("enter a number"))
if num>0:
    print("the number is positive")
elif num<0:
    print("the number is negative")
else:
    print("the number is zero")'''
    
#write a program to check grater no amoungs these three numbers
'''x=int(input("enter a number"))
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
        print("greter number is (z)",z)'''
        
# wap to check a person is eligible to vote or not
'''age=int(input("enter a age"))
if age>=18:
    print("you ara eligible to vote")
else:
    print("you are not eligible to vote")'''
    
#WAP to check given year is a leap year or not.
#year=int(input("enter a year"))
'''if (year% 4 ==0 and year % 100!= 0 )or (year % 400==0):
    print("its a leap year")
else:
    print("its not a leap year")'''
    
# WAP to check your gread based on your own score.
'''score=int(input("enter a gread:"))
if score>=90:
    print("you got an A.")
else:
    if score>=80:
        print("you got an B.")
    else:
        if score>=70:
            print("you got score C.")
        else:
            if score>=60:
                print("you got score D.")
            else:
                if score>=50:
                    print("you got score D.")
                else:
                    print("you got score F.")'''
                    
# WAP to choose value within range of 0 to 4.
'''print("plese enetr the value from 0 to 4")
x=int(input("enter a number"))
if x==0:
    print("you entered :",x)
elif x==1:
    print("you entered :",x)
elif x==2:
    print("you entered :",x)
elif x==3:
    print("you entered :",x)
elif x==4:
    print("you entered :",x)
else:
    print("beyond the range then specified")
    '''
    
#WAP to calculater the square root of given number
'''num=float(input('enter a number:'))
num_sqrt=num**0.5
print('the squre root of num:',num_sqrt)

#WAP to find the area of triangle.
a=float(input("enter first side"))
b=float(input("enter first side"))
c=float(input("enter first side"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("the area of the triangle is:",area)'''

#python program to swap two variable
x=input("enter value of x:")
y=input("enter value of y:")
tem=x
x=y
y=tem
print("the value of x after swapping:{}".format(x))
print("the value of x after swapping:{}".format(y))

#WAP to check given no is prime not.
num=int(input("enter any number:"))
factor=0
if num