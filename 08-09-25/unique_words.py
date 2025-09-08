text=input("enter the text")

words=text.split(" ")
freq={}

for x in words:
    if(x in freq):
        freq[x]+=1
    else:
        freq[x]=1
        
print(freq)