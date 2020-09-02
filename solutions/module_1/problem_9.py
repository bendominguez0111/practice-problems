list_obj = [1, 2, 3, 56, 12, 23, 34, 12, 89, 90, 345, 67, 56, 34]

print('Max of the list:', max(list_obj))
print('Min of the list:', min(list_obj))
print('Range of the list:', (max(list_obj) - min(list_obj)))

# without using built-in functions
min_of_list = None
max_of_list = 0

for i in list_obj:

    if not min_of_list:
        min_of_list = i

    if i > max_of_list:
        max_of_list = i

    if i < min_of_list:
        min_of_list = i

print('Max of the list:', max_of_list)
print('Min of the list:', min_of_list)
print('Range of the list:', max_of_list-min_of_list)
