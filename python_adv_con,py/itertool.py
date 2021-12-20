from itertools import count, cycle, repeat

import time
#cy = cycle([1,2,3,4,5,6,7])    #1 2 3 4 5 6 7  1 2 3 4 ....                     # circular -->      iterable --> group of elements..
rp = repeat([1,2,3,4,5,6,7],times=5)    #1,2,3,4,5,6,7] [1,2,3,4,5,6,7]  [1,2,3,4,5,6,7]


for item in rp:
    print(item)
    time.sleep(0.4)


#cnt=count(25,1)

#for item in cnt:

 #   print("cnt",cnt)
  #  time.sleep(5)




    # cycle('ABCD') --> A B C D A B C D A B C D