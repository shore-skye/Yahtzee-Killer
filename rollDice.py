import random
min = 1
max = 6

def rollFiveDice():
    die1 = random.randint(min, max)
    die2 = random.randint(min, max)
    die3 = random.randint(min, max)
    die4 = random.randint(min, max)
    die5 = random.randint(min, max)

    roll = [die1, die2, die3, die4, die5]
    return roll