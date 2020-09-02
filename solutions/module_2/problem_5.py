players = [
            {
                'pos': 'RB',
                'pick': 90
            },
            {
                'pos': 'RB',
                'pick': 91
            },
            {
                'pos': 'WR',
                'pick': 92
            },
            {
                'pos': 'TE',
                'pick': 93
            },
            {
                'pos': 'RB',
                'pick': 94
            },
            {
                'pos': 'RB',
                'pick': 95
            },
            {
                'pos': 'WR',
                'pick': 96
            },
            {
                'pos': 'RB',
                'pick': 97
            },
            {
                'pos': 'TE',
                'pick': 98
            },
            {
                'pos': 'RB',
                'pick': 99
            },
            {
                'pos': 'QB',
                'pick': 100
            },
        ]

replacement_players = {}

for player in players:
    position = player['pos']
    replacement_players[position] = player['pick']

print(replacement_players)