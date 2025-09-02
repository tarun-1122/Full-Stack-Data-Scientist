p=int(input("enter principal amount"))
r=int(input("enter rate"))
t=int(input("enter time"))
type=input("enter the ttpe of intrest")
res=0
if(type=="simple"):
    res=(p*t*r)/100
elif type=="compound":
    res=(p*((1+r/100))**t)
    
print("res=",res)