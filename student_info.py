'''import time

count_seconds = 10
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>', flush = True)
		time.sleep(1)
	else:
		print('Start')

import operator
a={3:25,5:45,1:2,9:13}
#sorted_a=sorted(a.items(), key=operator.itemgetter(1))
#print("aceending",sorted_a)

sorted_a_decending=dict( sorted(a.items(), key=operator.itemgetter(1),reverse=True))
print("decendin",sorted_a_decending)
import copy
import operator

qulifierlist=[]
finalqulify=[]
cetscore=[]
finalcetscore=[]
num=int(input("Enter no of candidate:  "))
for item in range(num):
        name = (input('Enter candidate name:  '))
        rollno = (input('Enter candidate rollno:  '))
        phy=int(input('Enter phy score:  '))
        chem=int(input('Enter chem score:  '))
        math=int(input('Enter math score:  '))
        ttlperc = int(input('Enter total percentage:  '))
        cetscr = (input('Enter total cet score out of 200:  '))
        grouptotal=phy+chem+math
        print("grouptotal",grouptotal)

        if 100>=phy>=35 and 100>=chem>=35 and 100>=math>=35 and 300>=grouptotal>=150 :
                print("qulify for eng admission")
                #qulifierlist=[copy.copy(name)]
                qulifierlist.append(name)
                finalqulify = copy.copy(qulifierlist)

                cetscore.append(cetscr)
                finalcetscore=copy.copy(cetscore)

        else:
                print("Disqulify for eng admission OR Entered invalid score")
print("Qulifier list", finalqulify)
print("finalcetscre", finalcetscore)

f=open("abc.txt",'w')
a=[5,10,55,"aaa"]
f.write("sucess not come easy \n")
f.write("work hard and smart \n")
f.write("a \n",a)

f.close()'''
#import studentadd
#from studentadd import Student
import pickle
f=open("abc.txt",'w')
n=int(input('enter num of student:'))
class Tstd:

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def __str__(self):
            return f'''{self.__dict__}'''

    def __repr__(self):
            return str(self)

    for i in range (n):
        name=input("enter name of studen")
        rollno=int(input('enter roll no'))
        s=Tstd(name,rollno)
        pickle.dump(s,f)
print("student list")
