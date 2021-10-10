import random


def play():
    user = input("Whats your choice?\n 'r' rock, 'p' paper, 's' scissors \n").lower()
    computer = random.choice(['r', 'p', 's'])
    
    if(user == computer):
        return 'Its a tie'

    elif(isWon(user, computer)):
        return 'You won'

    return 'You lost'


def isWon(user,computer):
    if(user == 's' and computer== 'p') or\
        (user == 'p' and computer == 'r') or \
            (user == 'r' and computer == 's'):
                return True;
    return False;


print(play())