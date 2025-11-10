
#x=10
#y=20
#z=30
#print(x<y and y<z)
#print(x>y and y>z) 

#x=-10.0
#print(x)
#print(type(x))

#x=5+3j
#y=10.5+10.5j
#print(x,y)
#print(type(x),type(y))

#z=0+0j
#print(z)
#print (type(z))

#x=int()
#print(x)
#y=float()
#print(y)
#z=complex()
#print(z)

#x='python'
#y="java"
#z='''php'''
#print(x,y,z)

#s='''this is python class
#i love pyhton'''
#print(s,type(s))

#s='this is "pyhton" class'
#print(s,type(s))

#s="this is \"pyhton\" class"
#print(s,type(s))

#eval#
#x=input("enter a number")
#print(x)
#print(type(x))

#x=eval(input("enter a number:"))
#print(x,type(x))

#x=10
#y=20
#z=eval('x+y')
#print(z)

#x=10
#y='language'
#print(type(eval('x+y')))

#python variable declaration

#x,y,z=10,20,30
#print(x,y,z)

#x=y=z=10
#print(x,y,z)

#x=10
#y=10
#print(id(x),id(y))

#x=0.7
#y=0.7
#print(id(x),id(y))

#x=(10,20,30,'python')
#y= (10,20,30,'python')
#print(id(x),id(y))

#set
#x={10,20,30,'python'}
#y= {10,20,30,'python'}
#print(id(x),id(y))

#frozonset
x=frozenset({10,20,30,'python'})
y= frozenset({10,20,30,'python'})
print(id(x),id(y))

#dict:
x={'name':'neela','age':37}
x={'name':'neela','age':37}
y={'name':'neela','age':37}
print(id(x),id(y))

x=True
y=True
print(id(x),id(y))

x=None
y=None
print(id(x),id(y))


