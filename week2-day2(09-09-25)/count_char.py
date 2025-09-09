text=input("enter the text")
count={}
for x in text:
    if(x in count):
        count[x]+=1
    else:
        count[x]=1
        
print(count)
