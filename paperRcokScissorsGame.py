from random import randint

player = input('You can choose any one (rock or paper or scissors): ')
choosen = randint(1, 3)


if choosen == 1:
    computer = 'rock'
elif choosen == 2:
    computer = 'paper'
else:
    computer = 'scissors'

print("Computer choosen : ", computer)

print(player, 'vs', computer)

if computer == player:
    print('DROW')
elif player == 'rock' and computer == 'paper':
    print('Computer win')
elif player == 'rock' and computer == 'scissors':
    print('Player win')
elif player == 'paper' and computer == 'rock':
    print('Player win')
elif player == 'paper' and computer == 'scissors':
    print("Computer win")
elif player == 'scissors' and computer == 'rock':
    print('Computer win')
elif player == 'scissors' and computer == 'paper':
    print("Player win")
else:
    print("again try")