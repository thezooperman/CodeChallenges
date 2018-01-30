from itertools import combinations

v = [1, 1, 2, 3]
max_dist = 0
all_combination = list(combinations(v, 2))
for i, p in enumerate(all_combination):
    for j, q in enumerate(all_combination[i + 1:]):
        tmp = ((p[0] - q[0]) ** 2) + ((p[1] - q[1]) ** 2)
        if tmp > max_dist:
            max_dist = tmp
print(max_dist)
