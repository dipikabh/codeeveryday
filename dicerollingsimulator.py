import random

def roll_dice():
    """
        Stimulates a rolling dice and returns random numbers, assuming min to be 1 and max to be 6
    """

    sides = int(raw_input("How many sides are on your dice? "))

    rolling = True
    
    while rolling:
        input = raw_input("Ready to roll the dice? Press 'Enter' to roll or 'Q' to quit.")
        if input.lower() != "q":
            number = random.randint(1, sides)
            print "You rolled a", number
        else:
            rolling = False

    print "Thanks for playing"

roll_dice()