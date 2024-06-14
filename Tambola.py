#this is a code for generating a random set of numbers from 1-90 as i lack the tambola markers

import random

upr_lt=int(input("Enter upper limit of board:"))
lwr_lt=int(input("Enter lower limit of board:"))
lst=[]
for i in range(lwr_lt,upr_lt+1,1):
    lst.append(i)

while (lst!=[]):
    number=random.randint(lwr_lt,upr_lt)
    if number in lst:
        print("The number is", number)
        lst.remove(number)
        input("Press Enter to continue...")
    else:
        continue
    
print("Thanks for playing")
