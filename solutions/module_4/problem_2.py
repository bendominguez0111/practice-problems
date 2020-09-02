x = [12, 450, 45, 23, 12, 34]
y = [12, 345, 12, 5, 6, 11]

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

print(correlation(x, y))

# check your work using the code below
# import numpy as np
# print(np.corrcoef(x, y)[0, 1])


