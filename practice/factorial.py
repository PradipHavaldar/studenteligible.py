#Factorial finding by recursion method

def factorial(n):
    #if (n==0 or n==1):
    #    return 1
    #else:
     #   return n*factorial(n-1)
#num=5
#print("factorial of ",num ,"is" ,factorial(num))

    return 1 if (num==0 or num==1) else num*factorial(n-1)

num=5
print("factorial of ",num ,"is" ,factorial(num))








#Find th factorial of number

'''number=int(input("Enter number---->"))
factorial=1
if number<0:
    print("Factorial does not exist for negative number")

elif number==0:
    print("Fatorial of 0 is  -- 1")

else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("Factorial of ", number,"is",factorial) '''