# n=int(input("enter a number"))
# n=15
# print(n)

# x=int(input('Enter any no :---'))
# print(x)

def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
     fib(1000)
