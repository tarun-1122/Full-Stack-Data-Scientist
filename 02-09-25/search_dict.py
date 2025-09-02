Phonebook = {"Suhel": 9876543210, "Ravi": 9123456780, "Anita": 9988776655}

name=input("search name ")

for i in Phonebook:
    if(i.lower()==name):
        print("Phone number of ",name," is ",Phonebook.get(i))
        
