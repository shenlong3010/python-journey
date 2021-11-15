def quicksort(left, right, arr):
	if (left < right):
		p = partition(left, right, arr)
		quicksort(left, p - 1, arr)
		quicksort(p + 1, right, arr)


def partition(start, end, arr):
	pivot_idx = start
	pivot = arr[pivot_idx]
	while start < end:
		while start < len(arr) and arr[start] <= pivot:
			start += 1
		while arr[end] > pivot:
			end -= 1
		if (start < end):
			arr[start], arr[end] = arr[end], arr[start]
	arr[end], arr[pivot_idx] = arr[pivot_idx], arr[end]
	return end

arr = [10, 7, 8, 9, 1, 5]
quicksort(0, len(arr) - 1, arr)
print(arr)
