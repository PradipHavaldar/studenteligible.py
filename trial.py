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
print("decendin",sorted_a_decending)'''

num=int(input("Enter no of candidate:  "))
for item in range(num):



