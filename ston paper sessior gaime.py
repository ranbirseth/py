
print("for rock type 0 ,for sesior type 1, for paper type 2 ")

b=int(input("enter your number :-"))

import random
a=random.randint(0,2)
print(a)

if (a==0 and b==0):
    print("match drow")

if (a==0 and b==0):
    print("match drow")
if (a==1 and b==1):
    print("match drow")

if (a==2 and b==2):
    print("match drow")

if (a==0 and b==1):
    print("computer won")

if (a==0 and b==2):
    print("you won")

if (a==1 and b==0):
    print("you won")

if (a==1 and b==2):
    print("computer won")

if (a==2 and b==0):
    print("computer WON")

if (a==2 and b==1):
    print("you won")
