n=int(input("enter no ==="))

for poss,i in enumerate(range(0,n)):
    if poss==i:
        print("*")
        if i==poss:
            print("@")





    '''n=int(input("enter no ==="))

for i in range(n,0,-1):
    print("*"*i)

for i in range(0,n+1):
    print("*"*i)

'''


'''from collections import*

a=[5,6,7,6,8,7,9,5,5,6,"a",9,"a",9,"a"]

print(Counter(a))
print(OrderedDict(a))
'''



'''#accesissng Nested dict using for loop

frrate={'mango':{'hapus':'5000'},'apple':{'himalay':200},'banana':{'sangli':50}}

#for i in frrate:
    #print(i)

for i in frrate:
    for fruit in frrate[i]:
        #print('name of fruit special from',i,'=' ,fruit)
         for rate in frrate[i][fruit]:
             print(rate)
'''