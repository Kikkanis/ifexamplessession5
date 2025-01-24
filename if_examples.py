# lets create a virtual bartender that serves you if you are of legal age

from random import choice
drinks = ["whiskey", "beer", "gin served freshly", "vodka", "hennessy", "champagne", "sake", "rum"]
mixers = ["fanta limon", "tonic water", "red bull", "coca cola", "soda"]

print(f"{choice(drinks)} {choice(mixers)}")
print("i am the virtual bartender, welcome to my humble shitty bar")
name = input("How should i call you? ")

try:
    age = input("how old are you")
    age = int(age) # this is where we can have problems
    legal = None
    country = input("where are you from?")
    if age<18:
        legal = False
    elif age<20:
        if country == "Norway":
            legal = True
        else:
            Legal = False
    elif age < 14:
        if country == "Austria" or country == "Luxembourg":
            legal = True
        else:
            legal = False
    elif age < 21:
        if country == "USA" or country == "UAE":
            legal = False
        else:
            legal = True
    else: # For age greater than 21
        legal = True

    if legal:
        print(f"Here is a {choice(drinks)} {choice(mixers)}")
    else:
        print(f"I can only serve you {choice(mixers)}")


except ValueError:
    print(" i dont have time for your games! get out boy!")