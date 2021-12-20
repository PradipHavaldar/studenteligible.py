import sys

a=[1,5,6,2,3,'star']
b=(25,26,27)
a.extend(b)
print(a)
a.append('str')
print(a)
x=a.index(5)
print(x)
y=a.index('str')
print(y)
a.clear()
print(a)
a.extend(b)
print(a)
z=a.count(25)
print(a,z,b)
p=a.copy()
print(p)
print(a)

q=a.extend(p)
print(a,q)


print("----#-----")
a=[12,2,5,7,8,12,'%']
print(a)
X=a.extend([5,2,6,25])          #a=a.extend([5]) then ...print a= none why
print(a)
A=a.append(888)                    #a=a.append([888]) then ...print a= none why
print(a)
z=a.copy()
print(a)

z=a==a
print(z)
print(a)
w=[1,2,3]
q=w.append ['star']
print(w)

a=[4,5,8,9,6,1,2]
a1=a.copy()
print(a1)
