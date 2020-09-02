stats = {
    'Jameis Winston': {
        'passing_yds': [194, 208, 380, 385, 204, 400, 301, 335, 358, 313, 313, 268, 456, 458, 335, 201],
        'passing_td': [1, 1, 3, 4, 2, 1, 2, 2, 1, 2, 3, 0, 4, 4, 1, 2],
        'passing_int': [3, 0, 1, 1, 0, 5, 2, 0, 2, 4, 2, 0, 3, 1, 4, 2]
    },
    'Tom Brady': {
        'passing_yds': [341, 264, 306, 150, 348, 334, 249, 259, 285, 216, 190, 326, 169, 128, 271, 221],
        'passing_td': [3, 2, 2, 0, 3, 0, 1, 2, 1, 0, 1, 3, 1, 2, 1, 2],
        'passing_int': [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1]
    }
}

# zipping together all three passing fantasy categories.
# using the built-in zip function to allow us to do this
# https://www.programiz.com/python-programming/methods/built-in/zip

zipped_jameis_fantasy_points = zip(
    stats['Jameis Winston']['passing_yds'], 
    stats['Jameis Winston']['passing_td'], 
    stats['Jameis Winston']['passing_int']
)

jameis_fantasy_points = [yds/25 + td*6 + inter*-2 for yds, td, inter in zipped_jameis_fantasy_points]

zipped_brady_fantasy_points = zip(
    stats['Tom Brady']['passing_yds'], 
    stats['Tom Brady']['passing_td'], 
    stats['Tom Brady']['passing_int']
)

brady_fantasy_points = [yds/25 + td*6 + inter*-2 for yds, td, inter in zipped_brady_fantasy_points]

def compute_standard_deviation(data_set):
    mu = sum(data_set)/len(data_set)
    squared_deviations = [(x - mu)**2 for x in data_set]
    std_dev = (sum(squared_deviations)/len(data_set))**(1/2)

    return std_dev

print(
    'Jameis Winston\'s Mean Fantasy Output:', sum(jameis_fantasy_points)/len(jameis_fantasy_points), '\nJameis Winston\'s Standard Deviation for Fantasy Output:', compute_standard_deviation(jameis_fantasy_points)
)

print(
    'Tom Brady\'s Mean Fantasy Output:', sum(brady_fantasy_points)/len(brady_fantasy_points), '\nTom Brady\'s Standard Deviation for Fantasy Output:', compute_standard_deviation(brady_fantasy_points)
)

