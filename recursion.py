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

'''def natural_no(n):
    if n==0:
        return
    print(n)
    natural_no(2*-1)
    n=int(input("enter a number:"))
    natural_no(n)
    '''
#***********************************************************************************************
def sum_natural(n):
    if n == 1:      # base case
        return 1
    return n + sum_natural(n - 1)

# take input from user
num = int(input("Enter a number: "))

# call the function and print result
print("Sum =", sum_natural(num))

    
