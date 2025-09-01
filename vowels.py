x=input("enter the sentence")

vowels=['a','e','i','o','u','A','E','I','O','U']
vowels_count=0
consonants_count=0

for i in x:
    if i in vowels:
        vowels_count+=1
    else:
        consonants_count+=1

print("vowels=",vowels_count,"consonants=",consonants_count)
