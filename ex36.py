from sys import exit

def puppy_saved():
    print("After fashioning a front pack from window curtains, you climbed out the window and saved the puppy!")
    print("Congrats! Now go pay the vet bills...")
    print("How much can you afford?")

    money = int(input("> "))

    if money >= 400:
        print("You might actually be able to take care of this dog!!! YOU WIN!!!")
        print("Let's give the dog a name.")
        naming()
        exit(0)
    elif money < 400:
        print("You saved it this time, but it's gonna be a struggle...")
        print("Not quite a win which means you've lost. Better luck next time.")
        exit(0)
    else:
        print("Let's try that again.")
        puppy_saved()


def naming():
    names = ["Sebastian", "Seabass", "Seamus", "Little Shea"]

    print("These are probably the best names.")
    for name in names:
        print(name)
    print("So what do we call him???")

    name = input("> ")

    if name in names:
        print(f"Fantastic! He even looks like a {name}. Let's call it a day.")
        exit(0)
    else:
        print("After all that effort to save him, the dog runs off because you chose a bad name.")
        print("Even though you came this far, it sure feels like defeat...")
        print("Better luck next time.")
        exit(0)


def burning_house():
    print("You find yourself in a house surrounded by blazing fire.")
    print("What do you do? Get the hell out? Or check for survivors?")

    choice = input("> ")

    if "check" in choice:

        direction = up_or_down()

        print(f"Ok, headed {direction}.")

        return direction

    elif "out" in choice:
        print("You survived. Way to not be a hero. Lame.")
        exit(0)
    else:
        print("Not sure what you mean. Try again.")
        burning_house()


def up_or_down():
    print("You seem to be on the middle floor of the house, and have found stairs.")
    print("The fire is bad all over the place, but especially below, and you hear wood creaking...")
    print("Go up or down???")

    return input("> ")


def ending(direction):
    if "up" in direction:
        print("What the hell kind of door is that?!?!?")
        puzzle_door()
    if "down" in direction:
        print("Oh, this actually isn't too bad and nobody to save.")
        print("You walk out the front door and go home to a normal life of pergatory.")
        exit(0)


def puzzle_door():
    print("A weird voice comes out of a slightly melted speaker to the side of the door at the top of the stairs.")
    print("You've found the PUZZLE DOOR and must answer my riddle to pass.")
    print("Riddle me this...")
    print("Grandpa went out for a walk and it started to rain.")
    print("He didn't bring an umbrella or a hat. His clothes got soaked, but not a hair on his head was wet.")
    print("How is this possible?")

    answer = input("> ")

    if "bald" in answer:
        print("You're right!!! You may pass.")
        print("The door swings open, and you find the cutest little puppy that surely wouldn't have made it without you.")
        puppy_saved()
    else:
        print("Sucks to suck. You will now burn to death and save no one. Nice try. Goodbye.")
        exit(0)


def start():
    print("You wake up one morning and find a shimmering portal beside your bed.")
    print("It's a bit ominous, but reminds you of the video games you play.")
    print("Heros always jump through portals... Maybe you should too.")
    print("Stay and chillax like it never happened? Or jump through?")

    decision = input("> ")

    if "stay" in decision or "chillax" in decision:
        print("Looks like another normal day of normalcy. Enjoy pergatory.")
        exit(0)
    elif "jump" in decision or "through" in decision:
        "Buckleup!!!"
        path = burning_house()
        ending(path)
    else:
        print("Try again and answer carefully.")
        start()

start()
