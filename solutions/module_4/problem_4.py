def euclidean_dist(a, b):

    dist = sum(
        [(ai - bi)**2 for ai, bi in zip(a, b)]
        )**(1/2)

    return dist

dist = euclidean_dist((1.0, 450), (5.0, 340))
print(dist)

# check your work
# from scipy.spatial.distance import euclidean
# dist = euclidean((1.0, 450), (5.0, 340))
# print(dist)