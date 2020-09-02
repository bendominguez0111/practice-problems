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

max_rushing_yds = 0
max_rushing_yds_player = ''

for player in players:
    if player['rushing_yds'] > max_rushing_yds:
        max_rushing_yds = player['rushing_yds']
        max_rushing_yds_player = player['name']

print(max_rushing_yds_player, 'had the most rushing yds:', max_rushing_yds, 'yds')

"""
Alternate solution. Using the Python list method 
append
"""

