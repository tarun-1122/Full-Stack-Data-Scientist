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
if(prime(x)):
    print("it is a prime")
else:
    print("not a prime")

