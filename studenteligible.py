#from studentadd import Student
import studentadd
import copy
import operator
import pickle
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

scorecard=(dict(zip(finalqulify,finalcetscore)))
print("scorecard",scorecard)
sorted_merit_list=dict( sorted(scorecard.items(), key=operator.itemgetter(1),reverse=True))
print("merit list by CET score",sorted_merit_list)
print("Qulifier list", finalqulify)
print("finalcetscre", finalcetscore)
with open("abc.txt","w") as f:
        s=studentadd.Student(name,rollno,phy,chem,math,ttlperc,cetscr)
        pickle.dumps(s,f)
        print("text is ready")