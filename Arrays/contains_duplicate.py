''' Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct. '''
from time import time
import random

nums_l = [random.randint(1, 100) for i in range(1000)]

def brute_force(nums):
	'''
	Brute force solution (O(n)),  Space complexity O(n)

	'''
	nums_dict = {}
	for i in range(len(nums)):
		if nums_dict.get(nums[i], 'not_here') == 'not_here':
			nums_dict[(nums[i])] = True
		else:
			return True
	return False


def optimized_soln(nums):
	'''
	More optimized soltuion (O(n)),  Space complexity O(1)

	'''
	return True if len(set(nums)) < len(nums) else False


s1 = time()
print('Brute Force: O(n) solution')
print(brute_force(nums_l))
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: O(n) solution, O(1) Space complexity')
print(optimized_soln(nums_l))
print('Time Taken: ',(time()-s2))