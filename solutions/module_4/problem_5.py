positional_values = {
    'WR': 50,
    'RB': 32,
    'TE': 45,
    'QB': 110
}

players = [
    {
        'name': 'AJ Brown',
        'position': 'WR',
        'projected': 200
    },
    {
        'name': 'Aaron Jones',
        'position': 'RB',
        'projected': 220
    },
    {
        'name': 'Gardner Minshew',
        'position': 'QB',
        'projected': 245
    }
]

for player in players:

    position = player.get('position')

    projected = player.get('projected')

    positional_value = positional_values.get(position)

    value_score = projected - positional_value

    player['value_score'] = value_score

# find the player with the best value score
# key argument tells Python's sorted what key in our dictionary to sort on.
players = sorted(players, key=lambda player: player['value_score'], reverse=True)

for i, player in enumerate(players):
    rank = i + 1
    print('#{} Value Score: {} ({})'.format(rank, player.get('name'), player.get('value_score')))