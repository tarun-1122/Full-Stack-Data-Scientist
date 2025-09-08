text=input("enter the text to check for palindrome")

text=text.lower()
list1=[]
for i in text:
    if(i==" "):
        continue
    else:
        list1.append(i)

i=0
bool=True
j=len(list1)-1
while(i<j):
    if(list1[i]==list1[j]):
        i+=1
        j-=1
    else:
        bool=False
        break
        
if(bool):
    print(text," is a plaindrome")
else:
    print(text," not a palindrome")