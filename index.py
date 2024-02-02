import random

Computer = random.randint(1, 3)
Player = random.randint(1, 3)

if Computer == 1:
    print('Computer: Rock')
elif Computer == 2:
    print('Computer: Paper')
elif Computer == 3:
    print('Computer: Scissor')

if Player == 1:
    print('Player: Rock')
elif Player == 2:
    print('Player: Paper')
elif Player == 3:
    print('Player: Scissor')

if Computer == 1 and Player == 1:
    print('Tie')
elif Computer == 2 and Player == 2:
    print('Tie')
elif Computer == 3 and Player == 3:
    print('Tie')
elif Computer == 1 and Player == 2:
    print('Player wins')
elif Computer == 1 and Player == 3:
    print('Computer wins')
elif Computer == 2 and Player == 1:
    print('Computer wins')
elif Computer == 2 and Player == 3:
    print('Player wins')
elif Computer == 3 and Player == 1:
    print('Player wins')
elif Computer == 3 and Player == 2:
    print('Computer wins')








