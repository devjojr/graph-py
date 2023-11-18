# Graph Implementation

This repository contains an implementation of a Graph in Python. The implementation supports both directed and undirected graphs, along with unit tests to ensure its correctness.

## Method(s)

### Graph Class

`__init__`: Initializes an empty graph.

`add_node`: Adds a node to the graph.

`add_directed_edge`: Adds a directed edge from the source to the destination.

`add_undirected_edge`: Adds an undirected edge between the source and destination.

`print_graph`: Prints the nodes and their adjacency lists.

### Node Class

Represents a node in the graph with key, incoming edges count, adjacency nodes, adjacency weights, adding, and removing neighbors.

## Unit Tests

The `test_graph.py` file contains unit tests for the `Graph` class using the `unittest` module.
