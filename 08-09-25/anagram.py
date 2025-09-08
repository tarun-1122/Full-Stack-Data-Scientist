word2=(input("enter the words to check"))
word1=(input("enter the words to check"))

word1=word1.replace(" ","").lower()
word2=word2.replace(" ","").lower()

word3=sorted(word1)
word4=sorted(word2)

if(word3==word4):
    print(word1," ",word2," are anagrams")
else:
    print(word1," ",word2," are not anagrams")
