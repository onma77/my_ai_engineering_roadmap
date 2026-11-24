# GRAPH THEORY FOR MACHINE LEARNING
### Advanced Study and Mathematical Practice

## 1. Adjacency Matrix and Degree Calculation

An adjacency matrix represents the connections between nodes.

Given:

A =
[0  1  1  0]
[1  0  0  1]
[1  0  0  1]
[0  1  1  0]

The degree of each node is calculated by adding the values in its row.

Node A = 0 + 1 + 1 + 0 = 2

Node B = 1 + 0 + 0 + 1 = 2

Node C = 1 + 0 + 0 + 1 = 2

Node D = 0 + 1 + 1 + 0 = 2

Total degree = 2 + 2 + 2 + 2 = 8.

Number of edges = 8 / 2 = 4.

This demonstrates the handshake lemma:

Sum of degrees = 2E.

## 2. Degree Matrix and Graph Laplacian

The degree matrix is formed by placing each node's degree along the diagonal.

D =
[2  0  0  0]
[0  2  0  0]
[0  0  2  0]
[0  0  0  2]

The graph Laplacian is:

L = D - A

Therefore:

L =
[ 2  -1  -1   0]
[-1   2   0  -1]
[-1   0   2  -1]
[ 0  -1  -1   2]

The Laplacian helps reveal graph connectivity and disconnected components.

## 3. Eigenvalue Calculation

Eigenvalues help identify structural properties of a graph.

For the Laplacian above, the eigenvalues are:

λ = 0, 2, 2, 4

Observations:

- There is one zero eigenvalue.
- Therefore, the graph has one connected component.
- The second-smallest eigenvalue is 2.

Fiedler value = 2.

This indicates that the graph is connected and has measurable connectivity between its nodes.

## 4. Normalized Adjacency Matrix

Normalization helps prevent nodes with many connections from dominating message passing.

The simple row-normalization formula is:

A_norm = D⁻¹A

Since every node has degree 2:

D⁻¹ =
[0.5  0    0    0]
[0    0.5  0    0]
[0    0    0.5  0]
[0    0    0    0.5]

Therefore:

A_norm =
[0  0.5  0.5  0]
[0.5  0  0  0.5]
[0.5  0  0  0.5]
[0  0.5  0.5  0]

Each row sums to 1.

## 5. Message Passing Calculation

Assume the initial node features are:

A = [2, 0]

B = [0, 4]

C = [4, 2]

D = [2, 2]

Using the normalized adjacency matrix:

For node A:

(B + C) / 2

= ([0,4] + [4,2]) / 2

= [2,3]

For node B:

(A + D) / 2

= ([2,0] + [2,2]) / 2

= [2,1]

For node C:

(A + D) / 2

= ([2,0] + [2,2]) / 2

= [2,1]

For node D:

(B + C) / 2

= ([0,4] + [4,2]) / 2

= [2,3]

The new features are:

A = [2,3]  
B = [2,1]  
C = [2,1]  
D = [2,3]

This is one round of message passing.

## 6. Graph Traversal Complexity

Both BFS and DFS have a time complexity of:

O(V + E)

Given:

V = 4 nodes  
E = 4 edges

O(4 + 4) = O(8)

The actual complexity is expressed as O(V + E), rather than O(8), because it describes how the algorithm scales as the graph grows.

## 7. Key Mathematical Takeaways

1. Adjacency matrix represents connections.
2. Degree matrix measures node connectivity.
3. Laplacian = D - A.
4. Zero eigenvalues reveal connected components.
5. Fiedler value measures algebraic connectivity.
6. Normalization controls how neighboring information is aggregated.
7. Message passing updates node features using neighboring information.

## 8. Practice Calculations

1. A graph has 6 nodes and 7 edges. Calculate the sum of its degrees.

2. Given degrees [3, 2, 3, 2], calculate the total number of edges.

3. If a connected graph has Laplacian eigenvalues [0, 1.5, 2, 4], identify its Fiedler value.

4. A node has three neighbors with features [2,4], [4,2] and [6,3]. Calculate their mean feature vector.

5. If a graph has 5 disconnected components, how many zero eigenvalues should its Laplacian have?

6. Explain why normalized adjacency is useful in Graph Neural Networks.