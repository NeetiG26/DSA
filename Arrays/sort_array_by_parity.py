'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''

from time import time
import random

nums = [random.randint(0,1000) for i in range(30000)]

def brute_force(arr):
	'''
	Brute Force Soln Time Complexity O(n), Space Complexity O(1)

	check for odd numbers from end, even numbers from start, exchange whenever both the places have opposite parities
	'''

	p1 = 0
	p2 = len(arr) - 1
	while p1 < p2:
		if arr[p1]%2 == 1:
			if arr[p2]%2 == 0:
				arr[p1], arr[p2] = arr[p2], arr[p1]
				p1 = p1 + 1
				p2 = p2 - 1
			else:
				p2 = p2 - 1
		else:
			p1 = p1 + 1
	return arr

s1 = time()
print('Brute Force: O(n) solution, Space complexity O(1)')
print(brute_force(nums))
print('Time Taken: ',(time()-s1))