import collections

def topological_sort(vertices, edges):
	sortedOrder = []
	if vertices <= 0:
		return sortedOrder
	# 1. Initialize the graph
	inDegree = {i: 0 for i in range(vertices)} # count of incoming edges
	graph = {i: [] for i in range(vertices)} # adjacency list graph
	# 2. Build the graph
	for e in edges:
		parent, child = e[0], e[1]
		graph[parent].append(child) # put the child into it's parent's list
		inDegree[child] += 1 # increment child's inDegree
	print(graph)
	print(inDegree)
	# 3. Find all sources i.e., all vertices with 0 in-degrees
	src = collections.deque()
	for k in inDegree:
		if inDegree[k] == 0:
			src.append(k)
	# 4. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
	# if a child's in-degree becomes zero, add it to the sources queue
	while src:
		vertex = src.popleft()
		sortedOrder.append(vertex)
		for child in graph[vertex]: # get the node's children to decrement their in-degress
			inDegree[child] -= 1
			if inDegree[child] == 0:
				src.append(child)
	# topological sort is not possible as the graph has a cycle
	if len(sortedOrder) != vertices:
		return []
	return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  # print("Topological sort: " +
  #       str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  # print("Topological sort: " +
  #       str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
