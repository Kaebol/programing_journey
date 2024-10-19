import random
#program is case sensitive
def computer_guess(y):
    low = 1
    high = y
    feedback = " "
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high(H), too low(L), or correct??? (C) ")
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            #low += low ezt érdekes lehet kipróbálni
            low = guess + 1

    print(f"Yaay! The computer guessed your number, {guess} correctly!")

computer_guess(10000)