from collections import deque
def bfs(graph, start, search_value):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex == search_value:
            return True
        visited.add(vertex)
    
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


start = "F"
search_value = "B"
res = bfs(graph, start, search_value)

print(f"element {search_value} : {res}")


# output : element B : True

# https://www.youtube.com/watch?v=gXgEDyodOJU
# 9:54

# visualize how the entire process of finding "B" with the graph Visualization\