import numpy as np

input_file = "input.txt"

input_data = []
with open(input_file, 'r') as file:
    lines = file.readlines()
    input_data.extend([int(x) for x in l.strip().split(',')] for l in lines)
    
input_data = np.array(input_data)
    
test_data = np.array([
[162,817,812],
[57,618,57],
[906,360,560],
[592,479,940],
[352,342,300],
[466,668,158],
[542,29,236],
[431,825,988],
[739,650,466],
[52,470,668],
[216,146,977],
[819,987,18],
[117,168,530],
[805,96,715],
[346,949,466],
[970,615,88],
[941,993,340],
[862,61,35],
[984,92,344],
[425,690,689]])

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def get_distances(data, euclidean_distance):
    distances = []

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            dist = euclidean_distance(data[i], data[j])
            distances.append({(i, j): dist})
        
    distances.sort(key=lambda x: list(x.values())[0])
    return distances
        
def create_circuits(data):
    circuits = [{i} for i in range(len(data))]

# Create a mapping from node to circuit index
# We start with each node in its own circuit
    node_to_circuit = {i: i for i in range(len(data))}
    return circuits,node_to_circuit

def connect_nodes(data, max_connections):
    distances = get_distances(data, euclidean_distance)
    circuits, node_to_circuit = create_circuits(data)
    
    n_connections = 0
    for d in distances:
        node1, node2 = list(d.keys())[0]
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
        
        if n_connections >= max_connections:
            break
    
    
    circuits.sort(key=len, reverse=True)
    
    return len(circuits[0]) * len(circuits[1]) * len(circuits[2])

assert(connect_nodes(test_data, max_connections=10) == 40)

print(connect_nodes(input_data, max_connections=1000))
