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

mean = lambda arr: sum(arr) / len(arr)

def correlation(x, y):

    x_mu, y_mu = mean(x), mean(y)

    x_minus_mu = [x - x_mu for x in x]
    y_minus_mu = [y - y_mu for y in y]

    numerator = sum(
        [x*y for x, y in zip(x_minus_mu, y_minus_mu)]
    )

    x_minus_mu_squared = [x**2 for x in x_minus_mu]

    y_minus_mu_squared = [y**2 for y in y_minus_mu]

    denom = (sum(x_minus_mu_squared)*sum(y_minus_mu_squared))**(1/2)

    return numerator/denom

qb = {
    'passing_tds': [2, 3, 3, 0, 3, 4, 0, 2, 1, 0, 2, 2, 2, 1, 0, 1],
    'passing_yds': [304, 320, 304, 397, 330, 356, 159, 182, 311, 271, 312, 313, 210, 384, 313, 330],
    'passing_int': [2, 3, 1, 0, 1, 0, 1, 1, 0, 1, 2, 0, 0, 2, 0, 0],
    'rushing_yds': [24, 3, 3, 18, 7, 7, 2, 13, 0, 8, 21, 8, 27, 6, 0, 12],
    'rushing_tds': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'fumbles': [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0],
    'receiving_yds': [0 for _ in range(1, 17)],
    'receptions': [0 for _ in range(1, 17)],
    'receiving_tds': [0 for _ in range(1, 17)]
}

wr = {
    'passing_tds': [0 for _ in range(1, 17)],
    'passing_yds': [0 for _ in range(1, 17)],
    'passing_int': [0 for _ in range(1, 17)],
    'rushing_yds': [0 for _ in range(1, 17)],
    'rushing_tds': [0 for _ in range(1, 17)],
    'fumbles': [0 for _ in range(1, 17)],
    'receiving_yds': [123, 78, 99, 34, 145, 67, 56, 98, 105, 34, 12, 205, 90, 87, 78, 190],
    'receptions': [10, 4, 6, 2, 12, 7, 4, 3, 5, 10, 3, 1, 12, 5, 7, 15],
    'receiving_tds': [2, 0, 0, 0, 3, 1, 1, 0, 2, 0, 0, 3, 0, 0, 0, 2]
}

def get_weekly_fantasy_performance(player):

    for stat_category, stat_lines in player.items():
        player[stat_category] = [i*fantasy_weights[stat_category] for i in stat_lines]

    player_ff_adjusted_stats = tuple(player.values())

    #element-wise additon of the two lists
    return [sum(x) for x in zip(*player_ff_adjusted_stats)]

wr_ff_performance = get_weekly_fantasy_performance(wr)
qb_ff_performance = get_weekly_fantasy_performance(qb)

#.43 should be the answerr
print(correlation(wr_ff_performance, qb_ff_performance))