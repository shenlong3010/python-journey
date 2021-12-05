list1 = [1,3,4,5]  
list2 = [2,6,7,8]

# O(n + m) | O(n) - n + m because iteration of two lists, n space
def merge_lists(l1, l2):
	res = [0 for i in range(len(l1) + len(l2))]
	i1, i2, ires = 0, 0, 0
	while i1 < len(l1) and i2 < len(l2):
		if l1[i1] < l2[i2]:
			res[ires] = l1[i1]
			i1 += 1
		else:
			res[ires] = l2[i2]
			i2 += 1
		ires += 1
	while i1 < len(l1):
		res[ires] = l1[i1]
		i1 += 1
		ires += 1
	while i2 < len(l2):
		res[ires] = l2[i2]
		i2 += 1
		ires += 1
	return res

def merge_lists_inplace(l1, l2):
	i1, i2 = 0, 0
	while i1 < len(l1) and i2 < len(l2):
		if l1[i1] < l2[i2]:
			i1 += 1
		else:
			l1.insert(i1, l2[i2])
			i1 += 1
			i2 += 1
	if i2 < len(l2):
		l1.extend(l2[i2:])
	return l1

print(merge_lists(list1, list2))
print(merge_lists_inplace(list1, list2))