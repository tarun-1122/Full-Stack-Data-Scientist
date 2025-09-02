x=eval(input("enter the emarks of 5 students as list"))

max=x[0]
min=x[0]

for i in x:
    if(i>max):
        max=i
    if(i<min):
        min=i

sum=0
for i in x:
    sum+=i
    
print("maximum marks= ",max)
print("mainimum marks= ",min)
print("average marks= ",sum/5)