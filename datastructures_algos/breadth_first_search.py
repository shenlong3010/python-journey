graph = {
	'a': ['b','c'],
	'b': ['d','e'],
	'c': ['f'],
	'd': [],
	'e': ['f'],
	'f': [],
}

visited = []	# list to keep track of visited nodes.
queue = []		# initialize a queue

def bfs(visited, graph, node):
	visited.append(node)
	queue.append(node)

	while queue:
		curr_vertex = queue.pop(0)
		print(curr_vertex)
		for neighbor in graph[curr_vertex]:
			if neighbor not in visited:
				visited.append(neighbor)
				queue.append(neighbor)

start = 'a'
bfs(visited, graph, start)

