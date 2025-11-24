#recutsion
#WAP to print n natural no.
'''def natural_no(n):
    if n==0:
        return
    print(n)
    natural_no(n-1)
    n=int(input("enter a number:"))
    natural_no(n)
    '''
#*************************************************************************************************
'''def natural_no(n):
    if n==0:
        return
    print(n)
    natural_no(2*-1)
    n=int(input("enter a number:"))
    natural_no(n)
    '''
#***********************************************************************************************
'''def sum_natural(n):
    if n == 1:    
        return 1
    return n + sum_natural(n - 1)
num = int(input("Enter a number: "))

print("Sum =", sum_natural(num))
'''
#************************************************************************************************
'''def sum_natural(n):
    if n==1:
        return 1
    return 2*n +sum_natural(n-1)
n=int(input("enter a number"))
res=sum_natural(n)
print(res)'''

#*************************************************************************************************

def multi(n):
    if n==1:
        return 1
    return n*multi(n-1)
n=int(input("enter a number"))
res=multi(5)
print(res)

