### 1. Introduction
Graph theory represents relationships between data using nodes (vertices) and edges. It is used in social networks, road maps, molecules and Graph Neural Networks (GNNs).

### 2. Key Concepts

- **Adjacency Matrix:** Represents connections between nodes. 1 means a connection exists; 0 means no connection.
- **Degree:** Number of connections a node has.
- **BFS:** Explores neighboring nodes first using a queue.
- **DFS:** Explores deeply before backtracking using a stack.
- **Graph Laplacian:** Calculated as L = D - A. Used to study graph connectivity.
- **Message Passing:** Allows nodes to collect and aggregate information from their neighbors.

### 3. Rough Calculations

Given three connected nodes (A, B, C):

Degree:
- A = 2
- B = 2
- C = 2

Handshake Lemma:

Sum of degrees = 2 × number of edges

6 = 2 × 3 = 6 ✓

**Laplacian Calculation**

L = D - A

D =
[2  0  0]
[0  2  0]
[0  0  2]

A =
[0  1  1]
[1  0  1]
[1  1  0]

L =
[ 2  -1  -1]
[-1   2  -1]
[-1  -1   2]

### 4. Message Passing Calculation

Initial features:

A = [1, 0]  
B = [0, 1]  
C = [1, 1]

A = ([0,1] + [1,1]) / 2 = [0.5, 1]

B = ([1,0] + [1,1]) / 2 = [1, 0.5]

C = ([1,0] + [0,1]) / 2 = [0.5, 0.5]

### 5. Applications

- GNNs for learning from connected data.
- Spectral clustering for grouping related nodes.
- BFS and DFS for graph traversal.
- PageRank for ranking important nodes.

### 6. Conclusion

Graph theory provides the foundation for understanding connected data. Adjacency matrices, Laplacians, traversal algorithms and message passing are important building blocks of graph-based machine learning.