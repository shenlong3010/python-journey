graph = {
	'a': ['b','c'],
	'b': ['d','e'],
	'c': ['f'],
	'd': [],
	'e': ['f'],
	'f': [],
}

visited = set()

def dfs(visited, graph, start):
	if start not in visited:
		print(start)
		visited.add(start)
		for neighbor in graph[start]:
			dfs(visited, graph, neighbor)

dfs(visited, graph, 'a')
		
