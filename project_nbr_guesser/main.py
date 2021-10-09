from random import randint


def Guesser(max_nbr):
    nbr = randint(1, max_nbr)
    guess = 0
    while guess != nbr:
        guess= int(input(f"Guess a number between 1 and {max_nbr} : "))
        if guess<nbr:
            print(f"{guess} is too low.")
        elif guess>nbr:
            print(f"{guess} is too high.")
    print(f"Yay! You guessed the number ({nbr}) correctly!")
    

def ComputerGuesser(max_nbr):
    low = 1
    high = max_nbr
    response = ''
    while response != 'c':
        if low != high:
            guess= randint(low, high)
        else:
            guess = low
        response= input(f"Is {guess} too low (l), too high (h) or correct (c)?").lower()
        if response == 'h':
            high = guess-1
        elif response== 'l':
            low = guess+1
    print(f"Yay! The computer guessed the number ({guess}) correctly!")


ComputerGuesser(100)
