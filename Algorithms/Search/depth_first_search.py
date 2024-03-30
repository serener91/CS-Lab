
def dfs(graph, start_node, visited_node=None):
    if visited_node is None:
        visited_node = set()

    visited_node.add(start_node)
    print(start_node, end=' ')  # Print the visited node

    # Recursion
    for neighbor in graph[start_node]:
        if neighbor not in visited_node:
            dfs(graph, neighbor, visited_node)


if __name__ == '__main__':

    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    # Starting node for DFS traversal
    start_node = 'A'

    print("Depth-First Search traversal starting from node", start_node)
    dfs(graph, start_node)
