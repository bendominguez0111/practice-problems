player = 'Josh Allen'

completions = 271
attempts = 461
yards = 3089
touchdowns = 20
interceptions = 9

passer_rating = ((
    ((completions/attempts) - 0.3) * 5 + \
    ((yards/attempts) - 3)*0.25 + \
    ((touchdowns/attempts)*20) + 2.375 - \
    ((interceptions/attempts) * 25)
) / 6) *  100

print('Josh allen had a passer rating of', passer_rating)