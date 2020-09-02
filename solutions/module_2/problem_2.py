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

# method number one.
# this is probably the preferred way to solve this problem, and definitely the cleanest approach.
# this approach will make more sense once you get to the Python crash course recap section.
def compute_fantasy_points(stats_dict):
    fantasy_points = sum(
        [stat*weight for stat, weight in zip(stats_dict.values(), fantasy_weights.values())]
    )
    return fantasy_points

print('Lamar Jackson\'s Fantasy Points scored for 2019:', compute_fantasy_points(lamar_jackson_stats))

# method number two.
# this approach is easier to understand, but also more combursome and less abstracted.
def compute_fantasy_points(stats_dict):

    return (
        stats_dict['passing_yds']*fantasy_weights['passing_yds'] + \
        stats_dict['passing_tds']*fantasy_weights['passing_tds'] + \
        stats_dict['passing_int']*fantasy_weights['passing_int'] + \
        stats_dict['rushing_yds']*fantasy_weights['rushing_yds'] + \
        stats_dict['rushing_tds']*fantasy_weights['rushing_tds'] + \
        stats_dict['fumbles']*fantasy_weights['fumbles'] + \
        stats_dict['receiving_yds']*fantasy_weights['receiving_yds'] + \
        stats_dict['receptions']*fantasy_weights['receptions']
    )

print('Lamar Jackson\'s Fantasy Points scored for 2019:', compute_fantasy_points(lamar_jackson_stats))
