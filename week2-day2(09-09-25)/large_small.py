no=eval(input("enter the numbers"))
max=no[0]
min=no[0]

for x in no:
    if(x>max):
        max=x
    if(x<min):
        min=x
print("max=",max," min=",min)
