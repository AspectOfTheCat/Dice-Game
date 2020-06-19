roll = input("Roll a 6 sided die, and tell me the number: ")

if roll > 6:
  print("Uh..no..")
  
elif roll < 1:
  print("You lost!")
  
else:

    print("Your roll is " + str(roll))

    print("Bot roll is..")

    from random import seed
    from random import choice
    seed()
    #The seed can be anything, but for the output to be different, the seed has to be different!
    botroll = choice(range(1,6,1))
    print(botroll)









