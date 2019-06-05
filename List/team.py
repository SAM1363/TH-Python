players = []
add_player = raw_input('Do you want to add a player to the team? Y/N ')
while add_player.lower() == 'y':
	player_name = raw_input('What player do you want to add? ')
	players.append(player_name)
	add_player = raw_input('Do you want to add another player to the team? Y/N ')

print('There are {} payler on the team'.format(len(players)))

player_number = 1
for player in players:
	print('Player NO{}, {}'.format(player_number, player))
	player_number += 1

goaly = raw_input('Who will be the goaly? select the number (1-{})'.format(len(players)))
goaly = int(goaly)

print('great! the goaly for the game will be {}'.format(players[goaly - 1]))