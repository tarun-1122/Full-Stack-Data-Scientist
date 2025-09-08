

def prime(n):
    if(n<=1):
        return False
    elif(n==2):
        return True
    elif(n>2 and n%2==0):
        return False
    i=3
    while i*i<n:
        if n%i==0:
            return False
        i+=2
    return True



x=int(input("enter the number"))

list=[]
for i in range(1,x):
    if(prime(i)):
        list.append(i)
        
print(list)
        