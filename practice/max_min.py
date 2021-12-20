n=['a','b','c']
print(n)
print(list(reversed(n)))



# Find length of list
'''from random import shuffle
mylist=[1,2,3,4,5,6,8,8,8]

count=0
for i in mylist:
    count+=1
print(count)
shuffle(mylist)
print(mylist)
'''







import sys
sys.exit(0)
li=[4,5,6,8,155,85,25,14]
#print(max(li))

max=li[0]
n=len(li)

for i in range(1,n):
    if li[i]>max:
        max=li[i]

print(max)


min=li[0]
m=len(li)

for i in range(1,m):
    if min>li[i]:
        min=li[i]

print(min)
