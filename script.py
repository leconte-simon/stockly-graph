import numpy as np

n = int(input())
shortcuts = [int(i) for i in input().split(" ")]

min_distances = [np.inf] * n

min_distances[0] = 0

for i in range(1, n):
    if max(min_distances) < np.inf:
        break

    # Select all nodes at distance i
    nodes_at_distance_i = [j for j in range(n) if min_distances[j] == i]

    # Update min_distances with natural path and shortcuts

    for node in nodes_at_distance_i:
        min_distances[node + 1] = min(min_distances[node + 1], min_distances[node] + 1)
        min_distances[shortcuts[node]] = min(min_distances[shortcuts[node]], min_distances[node] + 1)
    
min_distances.join(" ")

    