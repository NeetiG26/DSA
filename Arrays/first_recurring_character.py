'''Return the first recurring element, or undefined if no element recurs.'''
from time import time
import random

nums_l = [random.randint(1, 100) for i in range(1000)]

def brute_force(nums):
	'''
	Brute force solution Time Complexity O(n^2), Space Complexity O(1)

	'''
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if nums[i] == nums[j]:
				return nums[i]

	return 'undefined'

def optimized_soln(nums):
	'''
	More optimized soltuion Time complexity O(n),  Space complexity O(n)

	'''
	nums_dict = {}
	for i in range(len(nums)):
		if nums_dict.get(nums[i], 'not_here') == 'not_here':
			nums_dict[(nums[i])] = True
		else:
			return nums[i]
	return 'undefined'

print('Input:', nums_l)
s1 = time()
print('Brute Force: O(n^2) solution, O(1) Space Complexity')
print(brute_force(nums_l))
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: O(n) solution, O(n) Space complexity')
print(optimized_soln(nums_l))
print('Time Taken: ',(time()-s2))