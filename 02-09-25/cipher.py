text=input("enter the text")
shift=int(input("entre shift"))

for i in text:
    x=ord(i)
    shifted=x+shift
    shifted_char=chr(shifted)
    print(shifted_char,end="")
    