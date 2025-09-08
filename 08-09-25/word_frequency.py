from collections import Counter
text=input("enter the text")
words=text.lower().split(" ")
freq=Counter(words)
print(freq)