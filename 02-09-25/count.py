sentece=input("enter the sentence")

cwords=0
cvowels=0
ccharacters=0

list1=['a','e','i','o','u']

for i in sentece:
    ccharacters+=1
    if i in list1:
        cvowels+=1
        
        

list=sentece.split(" ")
cwords=len(list)
print("Total Words ",cwords)
print("Total vowels ",cvowels)
print("Total characters",ccharacters)
