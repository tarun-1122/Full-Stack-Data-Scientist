no=eval(input("enter list values"))

i=0
largest=no[0]
for i in no:
    if(i>=largest):
        largest=i
print("largest=",largest)