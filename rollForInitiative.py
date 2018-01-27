# Author: Louisa Katlubeck
# Date: 1/21/2018
# Description: rollForInitiative is a dice rolling application
# geared towards DnD and the similar games where the participants
# might not have their own dice with them. 
#
import random 

# find the dice to roll
diceSides = int(input('What sided dice would you like to roll (4, 6, 10, 20)?  '))

# find how many dice
numDice = int(input('How many of those dice would you like to roll?  '))

# make an array of possible dice numbers
diceArray = []
for j in range(1, diceSides):
    diceArray.append(j + 1)

# print the roll
for i in range(numDice):
    print("Roll", i + 1, "is", random.choice(diceArray))