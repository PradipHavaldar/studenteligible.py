name = (input('Enter candidate name:  '))
rollno = (input('Enter candidate rollno:  '))
phy = int(input('Enter phy score:  '))
chem = int(input('Enter chem score:  '))
math = int(input('Enter math score:  '))

ttlperc = float(input('Enter total  percentage:  '))
cetscr = int(input("enter cet score:  "))

grouptotal = phy + chem + math
print("grouptotal", grouptotal)
if phy >= 35 and chem >= 35 and math >= 35 and grouptotal >= 150 and ttlperc >= 50:
    print("Group qulify for eng admission")

else:
    print("disqulify")