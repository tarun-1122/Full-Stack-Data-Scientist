name=eval(input("enter the names of students"))

freq={}

for x in name:
    if(x in freq):
        freq[x]+=1
    else :
        freq[x]=1

for x in freq:
    if(freq[x]>1):
        print(x)
