'''
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
'''
from time import time
import random

nums = [random.randint(0,15) for i in range(10000)]
val = 4

def brute_force(arr, val):
	'''
	Brute force solution of Time Complexity O(n^2), Space Complexity O(1)
	'''

	n = arr.count(val)
	for i in range(n): #O(n)
		arr.remove(val) #O(n)
	return arr

def optimized_soln(arr, val):
	'''
	Optimized soln with TC O(n), SC O(1)
	'''
	i = 0
	for j in range(len(arr)):
		if arr[j] != val:
			arr[i] = arr[j]
			i = i+1
	return arr[:i]


s1 = time()
print('Brute Force: TC O(n^2), SC O(1)')
brute_force(nums,val)
print('Time Taken:', (time()-s1))
s2 = time()
print('Optimized Soln: O(n) solution, O(1) Space complexity')
optimized_soln(nums, val)
print('Time Taken: ',(time()-s2))