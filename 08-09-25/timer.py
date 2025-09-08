import time

t=int(input("enter the timer number"))

while t>0:
    time.sleep(1)
    print("time remaining is ",t)
    t-=1
    
print("times up")