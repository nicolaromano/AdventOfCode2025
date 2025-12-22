import numpy as np
import heapq

input_file = "input.txt"

input_data = []
with open(input_file, 'r') as file:
    lines = file.readlines()
    input_data.extend([int(x) for x in l.strip().split(',')] for l in lines)

input_data = np.array(input_data)

test_data = np.array([
    [162, 817, 812],
    [57, 618, 57],
    [906, 360, 560],
    [592, 479, 940],
    [352, 342, 300],
    [466, 668, 158],
    [542, 29, 236],
    [431, 825, 988],
    [739, 650, 466],
    [52, 470, 668],
    [216, 146, 977],
    [819, 987, 18],
    [117, 168, 530],
    [805, 96, 715],
    [346, 949, 466],
    [970, 615, 88],
    [941, 993, 340],
    [862, 61, 35],
    [984, 92, 344],
    [425, 690, 689]])


def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


def get_distances(data, euclidean_distance):
    distances = []

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            dist = euclidean_distance(data[i], data[j])
            heapq.heappush(distances, (dist, i, j))

    return distances


def create_circuits(data):
    circuits = [{i} for i in range(len(data))]

# Create a mapping from node to circuit index
# We start with each node in its own circuit
    node_to_circuit = {i: i for i in range(len(data))}
    return circuits, node_to_circuit


def connect_nodes(data, max_connections=-1):
    distances = get_distances(data, euclidean_distance)
    circuits, node_to_circuit = create_circuits(data)

    n_connections = 0

    while n_connections < max_connections or max_connections == -1:
        d = heapq.heappop(distances)

        node1, node2 = d[1], d[2]
        circuit1 = node_to_circuit[node1]
        circuit2 = node_to_circuit[node2]

        if circuit1 != circuit2:
            # Merge circuits
            circuits[circuit1].update(circuits[circuit2])

        # Update the node to circuit mapping
            for node in circuits[circuit2]:
                node_to_circuit[node] = circuit1

            circuits[circuit2] = set()

        n_connections += 1

        # If we only have 1 circuit left, we can stop
        if sum(bool(c) for c in circuits) == 1:
            # For part 2 we return the connection that made the full circuit
            return (node1, node2, d[0])

    circuits.sort(key=len, reverse=True)

    return circuits


circuits_test = connect_nodes(test_data, max_connections=10)
assert (len(circuits_test[0]) * len(circuits_test[1])
        * len(circuits_test[2]) == 40)

# Part 1
# circuits = connect_nodes(input_data, max_connections=1000)
# print(len(circuits[0]) * len(circuits[1]) * len(circuits[2]))

# Part 2 - merge until there is only 1 circuit left
node1, node2, distance = connect_nodes(input_data, max_connections=-1)

# get the x coordinates of the two nodes
x1 = input_data[node1][0]
x2 = input_data[node2][0]

print(x1 * x2)
