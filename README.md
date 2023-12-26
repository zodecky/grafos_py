# Graph Algorithms in Python

This project contains a Python implementation of various graph algorithms, including Dijkstra's algorithm for finding the shortest path between two nodes, Prim's algorithm for finding a minimum spanning tree, and a brute-force algorithm for finding the longest path between two nodes.

## Usage (grafos.py as main)

First, create a `Graph` object:

```python
g = Graph()
```


Add nodes with edges and weights:
```python
g.add_edge("1", "2", 0.1)
g.add_edge("2", "5", 0.2)
g.add_edge("5", "3", 5)
g.add_edge("3", "4", -9.5)
g.add_edge("4", "5", 2.3)
g.add_edge("1", "5", 1)
```

Or just add a node by itself and connect it later:
```python
g.add_node("1")
```
# Algorithms

## Shortest path
```python
path, distance = g.shortest_path("1", "3")
print("Path:", path)
print("Distance:", distance)
```

## Path from one node to all other nodes

```python
paths = g.path_to_all("1")
for node, (path, distance) in paths.items():
    print("Path from 1 to {}: {}, Distance: {}".format(node, path, distance))
```

## Minimum spanning tree
```python
mst = g.prim("1")
for frm, to, cost in mst:
    print("Edge from {} to {}, Cost: {}".format(frm, to, cost))
```

## Longest Path
```python
path, distance = g.longest_path("1", "3")
print("Path:", path)
print("Distance:", distance)
```

## Limitations
The longest_path method uses a brute-force approach that generates all paths from the start node to the end node and returns the longest one. This method can be very slow for large graphs or graphs with many paths between the start and end nodes. It's also not guaranteed to work correctly if the graph has cycles.
