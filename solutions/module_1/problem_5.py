players = [
    {
        'name': 'Derrick Henry',
        'rushing_yds': 1540,
        'rushing_att': 303
    },
    {
        'name': 'Aaron Jones',
        'rushing_yds': 1084,
        'rushing_att': 236,
    },
    {
        'name': 'Christian McCaffrey',
        'rushing_yds': 1387,
        'rushing_att': 287
    }
]

for player in players:

    player_name = player['name']

    yards_per_carry = player['rushing_yds'] / player['rushing_att']

    print(player_name, 'had a yards per carry in 2019 of', yards_per_carry)

