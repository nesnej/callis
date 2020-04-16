from random import randint


def generate_random_move():
    randomInt = randint(1, 4)
    if randomInt == 1:
        return "up"
    elif randomInt == 2:
        return "right"
    elif randomInt == 3:
        return "down"
    elif randomInt == 4:
        return "left"
    # Just in case let's always return a direction
    return "right"
