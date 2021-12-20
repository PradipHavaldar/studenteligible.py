class Student:

    def __init__(self,name,rollno,phy,chem,math,ttlperc,cetscr):
        self.name=name
        self.rollno=rollno
        self.chemistryscore=chem
        self.phyiscs=phy
        self.mathscore=math
        self.totalpercentage=ttlperc
        self.cetscore=cetscr
       # self.qulifylist=qulifylist
        #self.allqulify=allqulify

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)

#student1=Student

#s1=Student("anny",11,53,54,65,72,152)
#print("result of s1",s1)
#from studentadd import Student
import copy

num=int(input("Enter no of candidate:  "))
qulifierlist=[]
finalqulify=[]
cetscore=[]
finalcetscore=[]
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

                #nmescr=dict.fromkeys(finalqulify,finalcetscore)
                #nmescr1 = dict.fromkeys(finalqulify,cetscore )
                #print("name:score", nmescr)

        else:
                print("Disqulify for eng admission OR Entered invalid score")


print("Qulifier list", finalqulify)
print("finalcetscre", finalcetscore)
#print("name:score",nmescr)
#print("name:score",nmescr1)
print(dict(zip(finalqulify,finalcetscore)))

