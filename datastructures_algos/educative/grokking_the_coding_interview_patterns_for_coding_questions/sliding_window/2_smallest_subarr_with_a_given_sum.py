# O(n + n) = O(n) because while loop only processes each element once| O(1)
def smallest_subarray_with_given_sum(s, arr):
	winSum, winStart, min_length = 0, 0, float('inf')
	for winEnd in range(len(arr)):
		winSum += arr[winEnd]
		while winSum >= s:
			min_length = min(min_length, winEnd - winStart + 1)
			winSum -= arr[winStart]
			winStart += 1
	return 0 if min_length == float('inf') else min_length


print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2])) # 2
