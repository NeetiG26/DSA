''' Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target '''
from time import time

nums_l = [13,5,20,31,50,20,2,7,11,15]
target_num = 9

def brute_force(nums, target):
	'''
	Brute force solution (O(n^2))

	'''
	for i in range(len(nums)):
		for j in range(i, len(nums)):
			if nums[i] + nums[j] == target:
				return [i,j]

	return ('No pair makes the sum')
	

def optimized_soln(nums, target):
	'''
	More optimized soltuion (O(n))

	'''
	nums_dict = {}
	for i in range(len(nums)):
		if nums_dict.get(nums[i], 'not_here') == 'not_here':
			nums_dict[(target-nums[i])] = i

		else:
			return [i,nums_dict[nums[i]]]

	return ('No pair makes the sum')


s1 = time()
print('Brute Force: O(n^2) solution')
print(brute_force(nums_l, target_num))
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: O(n) solution')
print(optimized_soln(nums_l, target_num))
print('Time Taken: ',(time()-s2))

