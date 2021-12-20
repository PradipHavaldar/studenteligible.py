#Find factorial of number


#check no is  prime or nto,,,,, no==only two factor 1 and no itself

num=int(input("Enter number--",))
count=0

if num>1:
    for i in range(1,num+1):
            if(num%i)==0:
                count+=1

    if count==2:
        print(num,"Number is Prime")

    else:

        print(num,"Number is not Prime")






#SWAP 2 NO
num1=int(input("enter num1--"))
num2=int(input("enter num2--"))

print("Before swap",num1,num2)
num2,num1=num1 , num2


print("After swap",num1,num2)










import sys
sys.exit(0)
""""""
'''def deco():
    print('------------------------------')
deco()


@deco
def add(b,c):
    a=b+c
    return a
print(add(4,5))


@deco
def sub(z,y):
    x=z-y
    return x
print(sub(10,5))
'''
'''
a=[12,3,45,5,6,25]
a.reverse()
print(a)
'''
#start,*midle,end=li

#print(start)
#print(midle)
#print(end)







#count=0
#with open('text1') as today:
#from random import random, randint



'''
today=('TodaAy aAAA, ABC ,Def')

 
 for i in today:
    if i.isupper():
        count+=1
    print(count)
'''















'''from typing import Any, Iterator

list1 = [1, 2, 3, 4, 5, 6, 'a', 'b']
str1 = str([1223, 5666, 'abcf', 'ABCD', 'Wxyx'])

# print(list1[0:3])

# print(ord('a'))
# print(chr(110))

# print(4//1.5)
# print(4/1.5)
# print(5%2)
# print(unicodedata(15))

st1 = str(['abcd'])
st2 = str(['aa', 'bb', 'cc', 'dd'])
#print('+'.join(st1))
W=list(reversed(st1))
print(W)
'''