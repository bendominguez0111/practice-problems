lamar_jackson_stats = {
      'passing_yds': 3127,
      'passing_tds': 36,
      'passing_int': 6,
      'rushing_yds': 1206,
      'rushing_tds': 7,
      'fumbles': 8,
      'receiving_yds': 0,
      'receptions': 0,
      'receiving_td': 0
}

fantasy_weights = {
    'passing_yds': 0.04,
    'passing_tds': 4,
    'passing_int': -2,
    'rushing_yds': 0.10,
    'rushing_tds': 6,
    'fumbles': -2,
    'receiving_yds': 0.10,
    'receptions': 1, # adjust for half PPR and standard
    'receiving_td': 6
}

fantasy_points = (lamar_jackson_stats['passing_yds']*fantasy_weights['passing_yds'] + \
                lamar_jackson_stats['passing_tds']*fantasy_weights['passing_tds'] + \
                lamar_jackson_stats['passing_int']*fantasy_weights['passing_int'] + \
                lamar_jackson_stats['rushing_yds']*fantasy_weights['rushing_yds'] + \
                lamar_jackson_stats['rushing_tds']*fantasy_weights['rushing_tds'] + \
                lamar_jackson_stats['fumbles']*fantasy_weights['fumbles'] + \
                lamar_jackson_stats['receiving_yds']*fantasy_weights['receiving_yds'] + \
                lamar_jackson_stats['receptions']*fantasy_weights['receptions'])

print('Lamar Jackson\'s fantasy points scored for 2019:', fantasy_points)