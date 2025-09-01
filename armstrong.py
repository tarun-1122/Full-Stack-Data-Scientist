x=int(input("enter a number"))
temp=x
res=0
y=str(x)

digit=len(y)

while(temp>0):
    rem=temp%10
    res+=rem**digit
    temp//=10

if(res==x):
    print("it is armstrong number")
else:
    print("not an armstrong number")