''' Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct. '''
from time import time

nums_l = [0,13,5,20,31,50,20,2,7,0,11,15,0]

def brute_force(nums):
	'''
	Brute force solution (O(n))

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
	More optimized soltuion (O(n))

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