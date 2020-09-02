receiving_yards = [
    123, 89, 54, 95, 182, 89, 131, 112, 152, 114, 101, 48, 134, 128, 136, 37
]

# mu is the same thing as avg or mean
mu = sum(receiving_yards) / len(receiving_yards)

summed_squared_deviations = 0

for yard_total in receiving_yards:
    squared_deviation = (yard_total - mu)**2

    #iteratively add to the number above
    summed_squared_deviations = summed_squared_deviations + squared_deviation

# variance is the average squared deviation from the mean
variance = summed_squared_deviations / len(receiving_yards) 

#standard deviation is the square root of the variance
std_dev = variance**(1/2)

print(std_dev)