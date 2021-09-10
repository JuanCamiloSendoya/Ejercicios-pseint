#If condition
temperature = 35
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")


#¿what happen here?
temperature = 25
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")


#Ok, is done!
temperature = 25
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
    print("Done")

#elif / else
temperature = 25
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20: # (21, 30]
    print("It's a nice day")
elif temperature > 10: # (11, 20)
    print("It's a bit cold")
else:
    print("It's cold")
    print("Done")