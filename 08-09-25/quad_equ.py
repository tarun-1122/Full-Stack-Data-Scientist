import math

a=eval(input("ener a value"))
b=eval(input("ener b value"))
c=eval(input("ener c value"))

d=b*b-4*a*c

r1=(-b+math.sqrt(d))/(2*a)
r2=(-b-math.sqrt(d))/(2*a)

print("r1= ",r1)
print("r2=",r2)