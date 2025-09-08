import random
import string
def pass_generator(length):
    char=string.ascii_letters + string.digits + string.punctuation
    password=''.join(random.choice(char) for _ in range(length))
    return password
length=int(input("enter the length"))
passw=pass_generator(length)
print(passw)