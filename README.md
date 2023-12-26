# Graph Algorithms in Python

This project contains a Python implementation of various graph algorithms, including Dijkstra's algorithm for finding the shortest path between two nodes, Prim's algorithm for finding a minimum spanning tree, and a brute-force algorithm for finding the longest path between two nodes.

## Usage (readfile.py as main, with input files)

### Run
```shell
python readfile.py
```

The files to be opened are defined in the main function. In this example, 3 are used.

```python
def main() -> None:
    """Test the read_graph function."""
    read_and_print("grafo_W_1.txt")
    read_and_print("grafo_W_2.txt")
    read_and_print("grafo_W_3.txt")
```

## Alternative usage (grafos.py as main, no file as input)

### Run
```shell
python graph.py
```

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
mst = g.minimum_spanning_tree("1")
for frm, to, cost in mst:
    print("Edge from {} to {}, Cost: {}".format(frm, to, cost))
```

## Longest Path
```python
path, distance = g.longest_path("1", "3")
print("Path:", path)
print("Distance:", distance)
```

