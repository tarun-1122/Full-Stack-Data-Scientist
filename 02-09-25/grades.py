marks=int(input("enter the marks of the student"))

if(marks>=90 and marks<=100):
    print("A+")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<80):
    print("B")
elif(marks>=60 and marks<70):
    print("C")
elif(marks<60):
    print("Fail")