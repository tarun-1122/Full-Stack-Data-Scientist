import re

password=input("enter the password")
u=False
l=False
d=False
n=False

# if(len(password)<8):
    
for x in password:
    if(x.isdigit()):
        d=True
    elif(x.isupper()):
        u=True
    elif(x.islower()):
        l=True
    elif(x.isnumeric):
        n=True

if(d and u and l and n):
    print("it is strong password")
else:
    print('not strong password')