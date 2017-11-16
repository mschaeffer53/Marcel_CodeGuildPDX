import random

player_names = ['Matthew', 'Jean', 'Caroline', 'Adrienne', 'Rob', 'Dot', 'Roger', 'Gary', 'Julissa']
while True:
    num_players = int(input('How many players? '))
    if num_players < 3 or num_players >9:
        print('Fool! You can only play with 3-9 players.')
    else:
        break

def pick_players():
    players = []
    for player in range(num_players):
        player_name = random.choice(player_names)
        player_names.remove(player_name)
        num_chips = 3
        players.append({'name': player_name, 'chips':num_chips})
    return players

def roll_bones():
    faces = ['L', 'C', 'R', '.', '.', '.']
    roll = random.choice(faces)
    return roll

def chicken_dinner():
    winner = None
    for player in players:
        if player['chips'] > 0:
            if winner is None:
                winner = player
            else:
                return None
    return winner
pot = 0
players = pick_players()
player_id = 0

while True:
    player = players[player_id]
    num_chips = player['chips']
    player_left_id = player_id - 1
    player_right_id = player_id + 1
    if player_id == len(players):
        player_right_id = 0
    if num_chips >= 3:
        num_rolls = 3
    else:
        num_rolls = num_chips
    for roll in range(num_rolls):
        outcome = roll_bones()
        if outcome == 'C':
            pot += 1
            num_chips -= 1
        if outcome == 'R':
            players[player_right_id]['chips'] += 1
            num_chips -= 1
        if outcome == 'L':
            players[player_left_id]['chips'] += 1
            num_chips -= 1
    player['chips'] = num_chips
    winner_winner = chicken_dinner()
    if winner_winner is not None:
        print(winner_winner)
        break

    player_id += 1
    if player_id >= len(players):
        player_id = 0