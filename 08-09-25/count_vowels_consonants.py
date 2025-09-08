text=input("enter the text")

text=text.replace(" ","").lower()
count_v=0
count_c=0
vowels=['a','e','i','o','u']
for i in text:
    if(i in vowels):
        count_v+=1
    else:
        count_c+=1
        
print("vowels=",count_v," consonants=",count_c)