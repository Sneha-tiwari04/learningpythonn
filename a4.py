#decorater
# def outer_fun(var):
#     def inner_fun(x,y):
#         x=x+5
#         y=y+5
#         var(x,y)
#         return inner_fun
# @outer_fun
# def add(p,q):
#     print(p+q)
#     x=int(input("enter a number:"))
#     y=int(input("enter a number:"))
#     add(x+y)
    
# def outer_fun(var):
#     def inner_fun(x,y):
#         var(x)
#         return inner_fun
# @outer_fun
# def add(n):
#     x=range(2,n+1,2)
#     return list(x)
# n=int(input("enter a number:"))
# res=add(n)
# print(res)

# def generate_numbers(n):
#     for i in range(n):
#         yield i

# for x in generate_numbers(100000):
#     print(x)

# x=range(1000)
# print(list(x))

def gen_number(n):
    i=1
    while i<=n:
        yield i
n=int(input("enter a number"))
var=gen_number(n)
print(var)
print(list(var))
