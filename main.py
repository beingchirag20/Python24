'''
r = Rock
p = Paper
s = Scissor
'''

import random
computer = random.choice([-1,0,1])

youstr = input("Enter your choice:")
youdict = {"r": 1, "p": -1, "s": 0}
revdict = {1: "Rock", -1: "Paper", 0: "Scissor"}

you = youdict[youstr]

print("You chose: ", revdict[you])
print("Computer chose: ", revdict[computer])

if(computer == you):
    print("It's a tie")

else:
    if(computer == 1 and you == 0):
        print("Computer wins")
    elif(computer == -1 and you == 1):
        print("Computer wins")
    elif(computer == 0 and you == -1):
        print("Computer wins")
    elif(computer == 0 and you == 1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("You win")
    elif(computer == 1 and you == -1):
        print("You win")

