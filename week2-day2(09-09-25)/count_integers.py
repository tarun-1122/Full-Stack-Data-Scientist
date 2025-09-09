num=eval(input("enter the numbers"))
cp=0
cn=0
co=0
for x in num:
    if(x==0):
        co+=1
    elif(x>0):
        cp+=1
    else:
        cn+=1
print("cp=",cp," cn=",cn," co=",co)
