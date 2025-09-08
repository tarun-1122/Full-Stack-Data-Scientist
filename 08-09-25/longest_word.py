text=input("enter he text ")

words=text.split(" ")
res=''

max=0
for i in words:
    if(len(i)>max):
        max=len(i)
        res=i
print(res)