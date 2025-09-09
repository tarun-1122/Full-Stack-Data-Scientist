import math

a=eval(input("enter the first no"))
b=eval(input("enter the second no"))

while(True):
    ch=int(input("enter the nmber to apply operations"))
    if(ch<1 or ch>4):
        exit(0)
    else:
        if(ch==1):
            print(f"addition of two no {a}and {b} is {a+b}")
        elif(ch==2):
            print(f"subtraction of two no {a}and {b} is {a-b}")
        elif(ch==3):
            print(f"multiplication of two no {a}and {b} is {a*b}")
        elif(ch==4):
            print(f"division of two no {a}and {b} is {a/b}")
        else:
            print("invalid oeration")
   

    