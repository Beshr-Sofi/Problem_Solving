"""
Given a reference of a node in a connected undirected graph, return a deep copy
(clone) of the graph. Each node in the graph contains a value (int) and a list
of its neighbors (List[Node]).

Key Concepts & Challenges:
--------------------------
1. Deep Copy vs. Shallow Copy:
   - A shallow copy copies references to original nodes, so changes to the copy
     affect the original.
   - A deep copy creates entirely new Node instances for every node and recreates
     the identical edge connections between those new instances.

2. Cycles & Infinite Recursion:
   - Undirected graphs have cycles (e.g., Node 1 is a neighbor of Node 2, and
     Node 2 is a neighbor of Node 1).
   - Traversing without keeping track of visited nodes leads to infinite recursion
     and a stack overflow.

3. The Hash Map (Visited Dictionary):
   - We maintain a map `visited = {original_node: cloned_node}`.
   - Purpose:
     a) Avoid revisiting nodes and getting stuck in infinite loops.
     b) Provide references to already-created cloned nodes when building neighbor lists.

Algorithm (Depth-First Search - DFS):
-------------------------------------
1. Base Case: If the input node is None, return None.
2. If the current node is already in `visited`, return its cloned counterpart.
3. Otherwise:
   - Create a new node with the current node's value: `new = Node(node.val)`.
   - Record it immediately in `visited[node] = new` before visiting neighbors to
     handle cyclic references properly.
   - Iterate through each neighbor in `node.neighbors`, recursively calling `dfs`,
     and append the returned clone to `new.neighbors`.
4. Return the clone of the starting node.

Complexity Analysis:
--------------------
- Time Complexity: O(V + E)
  Where V is the number of vertices (nodes) and E is the number of edges.
  Every node is visited once, and each edge is processed during neighbor traversal.

- Space Complexity: O(V)
  - O(V) space for the `visited` dictionary storing mappings for all nodes.
  - O(V) recursion call stack depth in the worst-case (e.g., a straight line/path graph).
"""


class Node:
    """Represents a node in an undirected graph."""
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    """
    Creates a deep copy of an undirected graph using Depth-First Search (DFS).
    
    :param node: Node - Reference node in the original graph.
    :return: Node - Reference to the corresponding cloned node.
    """
    if not node:
        return None

    # Maps original node references to their corresponding cloned instances: {original_node: cloned_node}
    visited = {}

    def dfs(node):
        # If node has already been cloned, return the existing clone to prevent cycles
        if node in visited:
            return visited[node]
        
        # 1. Create a new node with the same value
        new = Node(node.val)
        # 2. Save to visited map immediately before recursing on neighbors (breaks cycles)
        visited[node] = new

        # 3. Recursively clone each neighbor and connect them to the new node
        for i in node.neighbors:
            new.neighbors.append(dfs(i))
        
        return new
    
    return dfs(node)

def printGraph(graph):
    """Helper function to print node values using BFS traversal."""
    visited = set()
    q = [graph]
    while q:
        node = q.pop(0)
        if node.val in visited:
            continue
        visited.add(node.val)
        q.extend(node.neighbors)
    
    for i in visited:
        print(i, end=" ")
    print()

def main():
    graph = Node(1)
    graph.neighbors = [Node(2), Node(4)]
    graph.neighbors[0].neighbors = [Node(1), Node(3)]
    graph.neighbors[1].neighbors = [Node(1), Node(3)]
    graph.neighbors[0].neighbors[1].neighbors = [Node(2), Node(4)]
    graph.neighbors[1].neighbors[1].neighbors = [Node(2), Node(4)]
    
    clone = cloneGraph(graph)
    printGraph(graph)
    printGraph(clone)

if __name__ == "__main__":
    main()
