from collections import deque


def bfs(graph, start):

    # Create a visited set to keep track of visited nodes to avoid revisiting them
    visited = set()

    # Create a queue to store nodes to be visited next
    # Enqueue the starting node into the queue
    queue = deque([start])

    # While the queue is not empty
    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')  # Print the visited node
            # Visit the dequeued node
            visited.add(node)
            # Enqueue all its unvisited neighbors into the queue
            queue.extend(graph[node])


# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Starting node for BFS traversal
start_node = 'A'

print("Breadth-First Search traversal starting from node", start_node)
bfs(graph, start_node)
