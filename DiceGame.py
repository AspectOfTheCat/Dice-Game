roll = input("Roll a 6 sided die.")

print("Your roll is" + str(roll))

print("Bot roll is..")

from random import seed
from random import choice
seed(1)
sequence = [i for i in range(20)]
for _ in range(1):
        selection = choice(sequence)
        print(sequence)









