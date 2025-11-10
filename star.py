# n=int(input("enter how many rows you required:"))
# i=1
# while(i<=n):
#     print('*'*n)
#     i=i+1

# n=int(input("enter how many rows you required:"))
# i=1
# while(i<=n):
#     print('*'*i+''*(n-1))
#     i=i+1

# n=int(input("enter how many rows you required:"))
# i=1
# while(i<=n):
#     print(' '*(n-i)+'* '*i)
#     i=i+1

# n=int(input("enter how many rows you required:"))
# i=0
# while(i<=n):
#     print(' '*i+'* '*(n-i))
#     i=i+1
# n=int(input("enter how many rows you required:"))
# i=n
# while(i>=1):
#     print('* '*i)
#     i=i-1 

n=int(input("enter how many rows you required:"))
i=1
while(i<=n):
    print(' '*+(n-i)+'* '*i)
    i=i+1
i=i-2
while(i>=1):
    print(' '*(n-i)+'* '*i)
    i=i-1