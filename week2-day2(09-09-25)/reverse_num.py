no=int(input("enter the number"))

res=0
while(no>0):
    rem=no%10
    res*=10
    res+=rem
    no//=10
print(res)