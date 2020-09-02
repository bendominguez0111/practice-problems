
todd_gurley_yards = [
    97, 63, 43, 16, 51, 41, 44, 73, 97, 22, 95, 79, 20, 48, 68
]

def compute_standard_deviation(data_set):

    mu = sum(data_set)/len(data_set)

    squared_deviations = [(x - mu)**2 for x in data_set]

    std_dev = (sum(squared_deviations)/len(data_set))**(1/2)

    return std_dev

# you can check your answer by using the numpy.std function
# import numpy as np
# print(np.std(todd_gurley_yards))

print(compute_standard_deviation(todd_gurley_yards))