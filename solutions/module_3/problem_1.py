fantasy_weights = {
    'passing_yds': 0.04,
    'passing_tds': 4,
    'passing_int': -2,
    'rushing_yds': 0.10,
    'rushing_tds': 6,
    'fumbles': -2,
    'receiving_yds': 0.10,
    'receptions': 1, # adjust for half PPR and standard
    'receiving_tds': 6
}

class Player2019:

    def __init__(self, name, position, rushing_yds, rushing_tds, receiving_yds, receiving_tds, receptions, passing_yds, passing_tds, passing_int, interceptions, fumbles):

        self.name = name

        self.position = position

        self.fantasy_stats = {
            'rushing_yds': rushing_yds,
            'rushing_tds': rushing_tds,
            'receiving_yds': receiving_yds,
            'receiving_tds': receiving_tds,
            'receptions': receptions,
            'passing_yds': passing_yds,
            'passing_tds': passing_tds,
            'passing_int': passing_int,
            'interceptions': interceptions,
            'fumbles': fumbles,
        }
        

    @property
    def fantasy_points(self):
        return sum(
            [self.fantasy_stats[stat_category]*weight for stat_category, weight in fantasy_weights.items()]
        )

#these are made up player stats
player = Player2019(
    name='Aaron Jones',
    position='RB',
    rushing_yds=1000,
    rushing_tds=6,
    receiving_yds=450,
    receiving_tds=6,
    receptions=45,
    passing_yds=0,
    passing_tds=0,
    passing_int=0,
    interceptions=0,
    fumbles=4
)

print(player.fantasy_points)