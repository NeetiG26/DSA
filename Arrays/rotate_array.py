'''Given an array, rotate the array to the right by k steps, where k is non-negative.'''
from time import time

nums_l = [1,2,3,4,5,6,7]
k_l = 3

def brute_force(nums, k):
	'''
	Brute force solution (O(n)), Space Complexity O(n)

	'''
	len_nums = len(nums)
	res = [0]*len_nums
	for i in range(len_nums):
		n = (i+k)%len_nums
		res[n] = nums[i]
	return(res)

def optimized_soln(nums, k):
	'''
	More optimized soltuion (O(n)), Space Complexity O(1)
	Using Cyclic replacements

	'''
	n = len(nums)
	k = k%n #precautionary check
	start = 0
	count = 0
	while count < n:
		current, prev = start, nums[start]
		while True:
			next_idx = (current+k)%n
			nums[next_idx], prev = prev, nums[next_idx]
			current = next_idx
			count = count + 1
			if start == current:
				break
		start = start + 1
	return nums


s1 = time()
print('Brute Force: O(n) solution, Space O(n)')
print(brute_force(nums_l, k_l))
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: O(n) solution, O(1) Space complexity, using cyclic replacements')
print(optimized_soln(nums_l, k_l))
print('Time Taken: ',(time()-s2))