import random

num=int(input("enter :"))
guess=random.randint(1,10)
print("random number",guess)

if num==guess:
        print("match")
    
else:
     print("not")
    