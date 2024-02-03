import random

while True:

    endGame = input('Would you like to play? (yes/no) ').lower()

    if endGame == 'yes':
        Player = input('Rock, Paper, Scissor? ').lower()
        Computer = random.randint(1, 3)

        if Computer == 1:
            print('Computer: Rock')
        elif Computer == 2:
            print('Computer: Paper')
        elif Computer == 3:
            print('Computer: Scissor')

        if Player == 'rock':
            print('Player: Rock')
        elif Player == 'paper':
            print('Player: Paper')
        elif Player == 'scissor':
            print('Player: Scissor')

        if Computer == 1 and Player == 'rock':
                print('Tie')
        elif Computer == 2 and Player == 'paper':
            print('Tie')
        elif Computer == 3 and Player == 'scissor':
            print('Tie')
        elif Computer == 1 and Player == 'paper':
            print('Player wins')
        elif Computer == 1 and Player == 'scissor':
            print('Computer wins')
        elif Computer == 2 and Player == 'rock':
            print('Computer wins')
        elif Computer == 2 and Player == 'scissor':
            print('Player wins')
        elif Computer == 3 and Player == 'rock':
            print('Player wins')
        elif Computer == 3 and Player == 'paper':
            print('Computer wins')

    elif endGame == 'no':
        print('Thank you for playing!!')
        break
        



