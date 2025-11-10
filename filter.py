# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = list(filter(lambda x: x % 2 == 0,numbers))
# odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)

# x=input("enter a value:")
# def firstname(n):
#     if n in('a','e','i','o','u','A','E','I','O','U'):
#         return n
# res=list(filter(firstname,x))
# print(''.join(res))

# s=input("enter a value:")
# s1=0
# for i in s:
#     if i in('a','e','i','o','u','A','E','I','O','U'):
#      s1=''.join(s1,i)
# print(s1)
    
# import functools
# l=[1,2,3,4,5,6,7]
# def sum(x,y):
#     print(x,y)
#     return x+y
# res=functools.reduce(sum,l,0)
# print(res)

# import functools
# l=[1,2,3,4,5,6,7]
# def sum(x,y):
#     print(x,y)
#     return x+y
# res=functools.reduce(sum,l)
# print(res)

#maximum
# import functools
# l=[10,20,40,6,78,90]
# def maxdigit(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# res=functools.reduce(maxdigit,l)
# print(res)

# import functools
# l=[10,20,40,6,78,90]
# def maxdigit(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# res=functools.reduce(maxdigit,l)
# print(res)

# x=lambda p,q,r :return p+q+r
# x(10,20,30)
# print(x(10,20,30))

# x=lambda x,y: x if x<y else y
# print(x(10,20))
    
# f=open("a1.txt",'at') 
# data="this is python class" 
# f.write(data)
# f.close()

# data1='''this is python and jango class\n'''
# f.write(data1)
# f.close()

# data2='java class'
# f.write(data2)
# f.close()

# f=open("a1.txt",'at')
# data="this is python class\n"
# data1='this is java class\n'
# data3='this is math class\n'
# f.writelines([data,data1,data3])
# f.close()

# f=open("a1.txt",'rt')
# data=f.read()
# print(data)
# f.close()

# f=open("a1.txt",'at')
# data="this is python class\n"
# data1='this is java class\n'
# data3='this is math class\n'
# f.writelines([data,data1,data3])
# f.close()

# f=open("a1.txt",'rt')
# data=f.read()
# print(data)
# f.close()
# print("data1:",data1)

# data=f.read(10)
# print(data)
# data1=f.read(15)
# print(data1)
# f.close()

# data=f.readline()
# print(data)
# f.close()

# data=f.readlines()
# print(data)
# f.close()

# with open('a1.txt','at')as f:
#     data='python'
#     f.write(data)
#     print(f.closed)
# print(f.closed)

# ***diffret b\w open()and with open()
# with open('a1.txt','rt')as f:
#     print(f.tell())
#     data=f.read(10)
#     print(data)
#     print(f.tell())

#seeks

# with open('n1.txt','ab+')as f:
#     print(f.tell())
#     data=b'this is python class'
#     f.write(data)
#     print(f.tell())
#     data1=f.read()
#     print(data1)
#     f.seek(0,0)
#     print(f.tell())
#     data2=f.read(20)
#     print(data2)
#     print(f.tell())

with open('n1.txt','rb+')as f:
    print(f.tell())
    f.read(10)
    print(f.tell())
    f.seek(-5,1)
    print(f.tell)