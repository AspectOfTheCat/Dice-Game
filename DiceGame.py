roll = input("Roll a 6 sided die, and tell me the number: ")

if int(roll) > 6:
  print("Uh..no..")
  
elif int(roll) < 1:
  print("You lost!")
  
else:

    print("Your roll is " + str(roll))

    print("Bot roll is..")

    from random import seed
    from random import choice
    seed()
    botroll = choice(range(1,6,1))
    print(botroll)
#Finally, done debugging this. This took a while. Enjoy!








