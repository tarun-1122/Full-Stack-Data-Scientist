def count_words(filename):
    
    
        with open(filename,'r') as file:
            text=file.read()
            words=text.split(" ")
            return len(words)
    
    # except:
    #     print("invalid file")
        
file_name=input("enter the filename")
print(file_name)
print(count_words(file_name))