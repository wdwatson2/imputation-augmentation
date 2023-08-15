from getpass import getpass as input

move1 = input('Player 1: ').lower()
move2 = input('\nPlayer 2: ').lower()

options = ['r', 'p', 's']

if ((move1 not in options) or (move2 not in options)):
    print('\nyou idiots')


else:
    #tie
    if (move1 == move2):
        print('\nTie')
    #player 1 wins
    elif ((move1 == 'r' and move2 == 's') or (move1 == 'p' and move2 == 'r') or (move1 == 's' and move2 == 'p')):
        print('\nPlayer 1 wins')
    else:
        print('\nPlayer 2 wins')

