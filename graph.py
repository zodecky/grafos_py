"""Graph data structure and algorithms."""

import heapq

class Graph:
    """
    Graph data structure.
    
    Stored as a dictionary of dictionaries. (like an adjacency list)
    """
    def __init__(self):
        """Initialize the Graph object."""
        self.nodes = {}

    def add_node(self, node: str):
        """Add a node to the graph."""
        self.nodes[node] = {}

    def add_edge(self, node_a: str, node_b: str, weight: float):
        """
        Connects two nodes.

        node_a: name of the first node
        node_b: name of the second node
        weight: weight/distance of the edge

        if the nodes are already connected, the weight is updated.

        if the node doesn't exist, it is created.
        """
        if node_a not in self.nodes:
            self.add_node(node_a)
        if node_b not in self.nodes:
            self.add_node(node_b)

        self.nodes[node_a][node_b] = weight
        self.nodes[node_b][node_a] = weight

    def get_nodes(self):
        """Return a list of nodes in the graph."""
        return self.nodes.keys()

    def get_edges(self, node: str):
        """Return a list of edges connected to the node."""
        return self.nodes[node].items()
    
    def print(self):
        """Print the graph."""
        for node in self.nodes.keys():
            print(node, "->", self.nodes[node])
    
    def dijkstra(self, start):
        """
        Implement Dijkstra's algorithm to find the shortest path from the 
        start node to all other nodes in the graph.

        Parameters:
        start (str): The starting node for Dijkstra's algorithm.

        Returns:
        distances (dict): A dictionary where the keys are nodes and the values
        are the shortest distances from the start node to the key node.
        previous_nodes (dict): A dictionary where the keys are nodes and the
        values are the previous nodes in the shortest path from the
        start node to the key node.
        """
        distances = {node: float('infinity') for node in self.nodes}
        previous_nodes = {node: None for node in self.nodes}
        distances[start] = 0
        queue = [(0, start)]
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            if current_distance > distances[current_node]:
                continue
            for neighbor, weight in self.nodes[current_node].items():
                distance = current_distance + abs(weight) # convert negative values to positive
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
        return distances, previous_nodes

    def shortest_path(self, start: str, end: str):
        """Find the shortest path using Dijkstra's algorithm.

        Parameters:
        start (str): The starting node for the path.
        end (str): The ending node for the path.

        Returns:
        path (list): A list of nodes representing the shortest path from the
        start node to the end node.
        distance (float): The total distance of the shortest path.
        """
        distances, previous_nodes = self.dijkstra(start)
        path = []
        while end is not None:
            path.append(end)
            end = previous_nodes[end]
        path.reverse()
        return path, distances[path[-1]]
    
    def path_to_all(self, start: str):
        """
        Find the shortest paths from the start node to all other nodes in the
        graph using Dijkstra's algorithm.

        Parameters:
        start (str): The starting node for the paths.

        Returns:
        paths (dict): A dictionary where the
        keys are nodes and the values are tuples.
        Each tuple contains a list of nodes representing the shortest path
        from the start node to the key node,
        and the total distance of the path.
        """
        distances, previous_nodes = self.dijkstra(start)
        paths = {}
        for node in self.nodes:
            path = []
            current_node = node
            while current_node is not None:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            path.reverse()
            paths[node] = (path, distances[node])
        return paths

    def longest_path(self, start: str, end: str):
        """
        Find the longest path from the start node to the end node using
        depth-first search with pruning.

        Parameters:
        start (str): The starting node for the path.
        end (str): The ending node for the path.

        Returns:
        longest (list): A list of nodes representing the longest path from the 
        start node to the end node.
        max_length (float): The total distance of the longest path.

        Extra: This was first implemented using recursion, but it caused a
        RecursionError for large graphs. So it was changed to a loop with a stack.
        """
        visited = set()
        stack = [(start, [start], 0)]
        longest, max_length = [], 0

        while stack:
            node, path, length = stack.pop()
            if node == end and length > max_length:
                longest, max_length = list(path), length
            elif node not in visited:
                visited.add(node)
                for neighbor, weight in self.nodes[node].items():
                    if length + weight > max_length:
                        stack.append((neighbor, path + [neighbor], length + weight))

        return longest, max_length
    
    def minimum_spanning_tree(self, start: str):
        """
        Compute the minimum spanning tree (MST) of the graph using Prim's algorithm.

        Parameters:
        start (str): The starting node for Prim's algorithm.

        Returns:
        mst (set): A set of tuples representing the edges in the MST. Each tuple contains two nodes (the ends of an edge) and the cost of the edge.
        """
        mst = set()
        visited = set([start])
        edges = [
            (cost, start, to)
            for to, cost in self.nodes[start].items()
        ]
        heapq.heapify(edges)

        while edges:
            cost, frm, to = heapq.heappop(edges)
            if to not in visited:
                visited.add(to)
                mst.add((frm, to, cost))
                for to_next, cost2 in self.nodes[to].items():
                    if to_next not in visited:
                        heapq.heappush(edges, (cost2, to, to_next))

        return mst


    

def main():
    """Print the graph."""
    g = Graph()
    g.add_edge("1", "2", 0.1)
    g.add_edge("2", "5", 0.2)
    g.add_edge("5", "3", 5)
    g.add_edge("3", "4", 9.5)
    g.add_edge("4", "5", 2.3)
    g.add_edge("1", "5", 1)
    g.print()

    path, distance = g.shortest_path("1", "3")
    print("Shortest path from 1 to 3: {}, Distance: {}".format(path, distance))

    paths = g.path_to_all("1")
    print("Shortest paths from 1 to all other nodes:")
    for node, (path, distance) in paths.items():
        print("Path from 1 to {}: {}, Distance: {}".format(node, path, distance))

    mst = g.minimum_spanning_tree("1")
    print("Minimum spanning tree:")
    for frm, to, cost in mst:
        print("Edge from {} to {}, Distance: {}".format(frm, to, cost))

    path, distance = g.longest_path("1", "3")
    print("Longest path from 1 to 3: {}, Distance: {}".format(path, distance))


if __name__ == "__main__":
    main()
