text=input("enter the text")

words=text.lower().split(" ")
freq={}

for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1
        
print(freq)
