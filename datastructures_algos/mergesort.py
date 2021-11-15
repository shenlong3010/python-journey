def mergesort(arr):
	if len(arr) > 1:
		mid = len(arr) // 2
		left = arr[:mid]
		right = arr[mid:]
		# Recursive call on each half
		mergesort(left)
		mergesort(right)
		# Two iterators for traversing the two halves and iterator for the main list
		i, j, k = 0, 0, 0
		while i < len(left) and j < len(right):
			if left[i] <= right[j]:
				# The vbalue from the left half has been used
				arr[k] = left[i]
				# Move the iterator forward
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			# Move to next slot
			k += 1

		# For all the remaining values
		while i < len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j < len(right):
			arr[k] = right[j]
			j += 1
			k += 1
arr = [5, 2, 1, 3]
mergesort(arr)
print(arr)
				
