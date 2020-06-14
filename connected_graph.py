"""
You are given an undirected connected graph.
An articulation point (or cut vertex) is defined as a
vertex which, when removed along with associated edges,
makes the graph disconnected (or more precisely, increases
the number of connected components in the graph). The task
is to find all articulation points in the given graph.

Input:
The input to the function/method consists of three arguments:

    numNodes, an integer representing the number of nodes in the graph.
    numEdges, an integer representing the number of edges in the graph.
    edges, the list of pair of integers - A, B representing an edge
    between the nodes A and B.

Output:
Return a list of integers representing the critical nodes.

Example:

Input: numNodes = 7, numEdges = 7,
edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

Output = [2, 3, 5]
"""

from typing import List
from collections import defaultdict

def build_graph(arr: List[List[int]]):
    graph = defaultdict(list)

    for record in arr:
        graph[record[0]].append(record[1])
        graph[record[1]].append(record[0])

    return graph

def dfs(node, graph, visited):
    if node in visited:
        return
    
    visited.add(node)
    for child in graph[node]:
        dfs(child, graph, visited)

def connected_graphs(arr: List[List[int]]):
    graph = build_graph(arr)

    nodes = len(arr)

    final_list = []
    
    # remove each vertex and check node count
    # if node count != 7, add the removed node
    for node in range(nodes):
        if node in graph:
            edges = graph[node]

            source = None
            # remove all edges from that node
            for edge in edges:
                graph[edge].remove(node)
                source = edge

            visited = set()
            # do a dfs/bfs to traverse graph
            dfs(source, graph, visited)

            # check if visited nodes == len(nodes) - 1
            if len(visited) != nodes - 1:
                final_list.append(node)

            # add removed node and its edges back
            for edge in edges:
                graph[edge].append(node)

    print(final_list)

if __name__ == "__main__":
    numNodes = 7
    numEdges = 7
    edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]

    connected_graphs(edges)