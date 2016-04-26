def dfs(graph, start):
    stack = [(None, start)]
    visited = set(start)

    while len(stack) > 0:
        parent, current = stack.pop(0)
        new_children = graph[current] - visited
        stack += ((current, child) for child in new_children)
        visited |= new_children


def bfs(graph, start):
    queue = [(None, start)]
    visited = set(start)

    while len(queue) > 0:
        parent, current = queue.pop(0)
        new_children = graph[current] - visited
        queue += ((current, child) for child in new_children)
        visited |= new_children

graph = {'A': {'B', 'C',’E'},
         'B': {'A','C', ‘D'},
         'C': {‘D'},
         'D': {‘C'},
         'E': {'F', ‘D'},
         'F': {‘C'}}
