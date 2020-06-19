roll = input("Roll a 6 sided die.")

print("Your roll is" + str(roll))

print("Bot roll is..")

from random import seed
from random import choice
seed(1)
#The seed can be anything, but for the output to be different, the seed has to be different!
sequence = [i for i in range(6)]
for _ in range(1):
        selection = choice(sequence)
        print(selection)









