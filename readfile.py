"""
Reads a file that describes a graph and returns a graph object.

The file must be in the following format:
n - number of nodes
a b c - node a is connected to node b with weight c
a b c
...
"""

import time
from graph import Graph
from typing import List


def read_graph(filename: str) -> Graph:
    """Read a graph from a file and return a graph object."""
    graph = Graph()
    with open(filename, "r", encoding="utf-8") as file:
        # The first line contains the number of nodes
        _ = int(file.readline()) # we don't need this value, because python is dynamic

        # The rest of the lines contain the edges
        for line in file:
            a, b, c = line.split()
            c = float(c)
            graph.add_edge(a, b, c)
    return graph


def read_and_print(filename: str) -> List[float]:
    """Read a graph from a file, print it, and return a list of times for each operation."""
    times = []
    graph = read_graph(filename)
    print(f"Reading {filename}")
    
    print("\n\n**********\n\n")

    clock = time.time()
    print("Shortest path from 1 to 10: Path - {}, Distance - {:.2f}".format(*graph.shortest_path("1", "10")))
    print("Shortest path from 1 to 20: Path - {}, Distance - {:.2f}".format(*graph.shortest_path("1", "20")))
    print("Shortest path from 1 to 30: Path - {}, Distance - {:.2f}".format(*graph.shortest_path("1", "30")))
    print("Shortest path from 1 to 40: Path - {}, Distance - {:.2f}".format(*graph.shortest_path("1", "40")))
    print("Shortest path from 1 to 50: Path - {}, Distance - {:.2f}".format(*graph.shortest_path("1", "50")))
    times.append(time.time() - clock)

    print("Time elapsed: {:.2f} seconds".format(times[-1]))

    print("\n\n**********\n\n")

    print("Minimum spanning tree:")
    clock = time.time()
    print(graph.minimum_spanning_tree("1")) # print option B
    times.append(time.time() - clock)

    print("Time elapsed: {:.2f} seconds".format(times[-1]))

    print("\n\n**********\n\n")

    print("Longest Paths: ")

    clock = time.time()
    print("Biggest distance from 1 to 10: {:.2f}".format(graph.longest_path("1", "10")[1]))
    print("Biggest distance from 1 to 20: {:.2f}".format(graph.longest_path("1", "20")[1]))
    print("Biggest distance from 1 to 30: {:.2f}".format(graph.longest_path("1", "30")[1]))
    print("Biggest distance from 1 to 40: {:.2f}".format(graph.longest_path("1", "40")[1]))
    print("Biggest distance from 1 to 50: {:.2f}".format(graph.longest_path("1", "50")[1]))
    times.append(time.time() - clock)

    print("Time elapsed: {:.2f} seconds".format(times[-1]))

    return times

def main() -> None:
    """Test the read_graph function."""
    time1 = read_and_print("grafo_W_1.txt")
    time2 = read_and_print("grafo_W_2.txt")
    # time3 = read_and_print("grafo_W_3.txt")

    print("\n\n**********\n\n")

    print("Total time elapsed for grafo_W_1.txt: {:.2f} seconds".format(sum(time1)))
    print(f"Shortest path: {time1[0]:.2f} seconds - Minimum spanning tree: {time1[1]:.2f} seconds - Longest path: {time1[2]:.2f} seconds\n")

    print("Time elapsed for grafo_W_2.txt: {:.2f} seconds".format(sum(time2)))
    print(f"Shortest path: {time2[0]:.2f} seconds - Minimum spanning tree: {time2[1]:.2f} seconds - Longest path: {time2[2]:.2f} seconds\n")

    # print("Time elapsed for grafo_W_3.txt: {:.2f} seconds".format(sum(time3)))
    # print(f"Shortest path: {time3[0]} seconds - Minimum spanning tree: {time3[1]:.2f} seconds - Longest path: {time3[2]} seconds\n")

if __name__ == "__main__":
    main()