from random import randint
moves = ['r','p','s']
r = ('rock')
p = ('paper')
s = ('scissors')
user_move = input('''
~~~~~~~CHOOSE YOUR MOVE~~~~~~~~
[R]OCK
[P]APER
[S]CISSORS
>>> ''')

def computer_move():
	moves_len = len(moves)
	move = randint(0, moves_len - 1)
	return move

if user_move == 'r' and computer_move() == len(moves[0]):
	print(f'Opponent did {r}')
	print('TIE')
elif user_move == 'p' and computer_move() == len(moves[0]):
	print(f'Opponent did {r}')
	print('WIN')
elif user_move == 's' and computer_move() == len(moves[0]):
	print(f'Opponent did {r}')
	print('LOSE')
elif user_move == 'r' and computer_move() == len(moves[1]):
	print(f'Opponent did {p}')
	print('LOSE')
elif user_move == 'p' and computer_move() == len(moves[1]):
	print(f'Opponent did {p}')
	print('TIE')
elif user_move == 's' and computer_move() == len(moves[1]):
	print(f'Opponent did {p}')
	print('WIN')
elif user_move == 'r' and computer_move() == len(moves[2]):
	print(f'Opponent did {s}')
	print('WIN')
elif user_move == 'p' and computer_move() == len(moves[2]):
	print(f'Opponent did {s}')
	print('LOSE')
elif user_move == 's' and computer_move() == len(moves[2]):
	print(f'Opponent did {s}')
	print('TIE')
elif user_move != 'r' or 'p' or 's':
	print('What?')