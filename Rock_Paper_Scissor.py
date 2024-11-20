# Rock Paper Scissor game

import random
print(f" Rock wins against Scissors \n Scissors will against Paper \n Paper wins against Rock")
print(f" 0.Rock\n 1.Paper\n 2.Scissors")
user_value = int(input("Enter the user value: "))
computer_value = random.randint(0,2)
if computer_value == user_value:
    print("lose")
