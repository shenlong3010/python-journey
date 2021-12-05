# O(n*k) | O(1)
def naive(k, arr):
	maxSubArr = 0
	for i in range(len(arr)-k+1):
		winSum = 0
		for j in range(i, i+k):
			winSum += arr[j]
		maxSubArr = max(winSum, maxSubArr)
	return maxSubArr

# O(n) | O(1)
def max_sub_array_of_size_k(k, arr):
	maxSum, winStart, winSum = 0, 0, 0
	for winEnd in range(len(arr)):
		winSum += arr[winEnd]
		if winEnd >= k - 1:
			maxSum = max(maxSum , winSum)
			winSum -= arr[winStart]
			winStart += 1
	return maxSum


print(naive(3, [2, 1, 5, 1, 3, 2])) # 9
print(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])) # 9
