def bs(arr, target):
	low = 0
	high = len(arr) - 1
	while low < high:
		# mid = low + ((high - low)/2)
		mid = (low + high) >> 1	
		print(mid, arr[mid])
		if arr[mid] < target:
			low = mid + 1	
		elif arr[mid] > target:
			high = mid - 1	
		else:
			return True 
	return False # cannot find

arr = [2, 3, 4, 10, 40]
x = 10
print(bs(arr, x))
