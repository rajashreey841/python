'''
Program_name: WAP which will select a random name from a list of names and the person selected will have to pay for eveybody's food bill:

'''
import random

Names = input("Enter the people name: ")
separate =  Names.split()
print("list= ", separate)
result = random.randint(0,len(separate)-1)
print(f" Index value: {result}\n {separate[result]} will pay the bill")

# or use choice function :--> print(random.choice(separate))