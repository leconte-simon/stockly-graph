import math

n = int(input())

# # -1 because index starts at 0
shortcuts = [int(i) - 1 for i in input().split(" ")]

min_distances = [math.inf] * n

min_distances[0] = 0
nodes_at_distance_i = [0]

for i in range(0, n):
    # if max(min_distances) < math.inf:
    #     break
    # Update min_distances with natural path and shortcuts
    nodes_at_distance_i_plus_1 = []
    for node in nodes_at_distance_i:
        if node != n-1:
            if i + 1 < min_distances[node + 1]:
                min_distances[node + 1] = i + 1
                nodes_at_distance_i_plus_1.append(node + 1)
        if node != 0:
            if i + 1 < min_distances[node - 1]:
                min_distances[node - 1] = i + 1
                nodes_at_distance_i_plus_1.append(node - 1)
        if i + 1 < min_distances[shortcuts[node]]:
            min_distances[shortcuts[node]] = i + 1
            nodes_at_distance_i_plus_1.append(shortcuts[node])
    
    nodes_at_distance_i = nodes_at_distance_i_plus_1
    
print(" ".join([str(i) for i in min_distances]))

    