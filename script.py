import numpy as np

n = int(input())

# -1 because index starts at 0
shortcuts = [int(i) - 1 for i in input().split(" ")]

min_distances = [np.inf] * n

min_distances[0] = 0

for i in range(0, n):
    # print(min_distances)
    # print(max(min_distances))
    if max(min_distances) < np.inf:
        break

    # Select all nodes at distance i
    nodes_at_distance_i = [j for j in range(n) if min_distances[j] == i]
    
    # Update min_distances with natural path and shortcuts

    for node in nodes_at_distance_i:
        min_distances[node + 1] = min(min_distances[node + 1], min_distances[node] + 1)
        min_distances[shortcuts[node]] = min(min_distances[shortcuts[node]], min_distances[node] + 1)
    
print(" ".join([str(i) for i in min_distances]))

    