'''
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
from time import time
import random

nums = [random.randint(0,100) for i in range(10000)]

def brute_force(arr):
	'''
	Brute Force solution with Time Complexity O(nlog(n)) and Space Complexity O(1)
	'''
	arr.sort()  #O(nlong(n))
	n = 0
	for i in range(len(arr)):
		if  arr[n] != arr[i]:
			n = n+1
			arr[n], arr[i] = arr[i], arr[n]
	return (n+1)


s1 = time()
print('Brute Soln: TC O(nlog(n)) SC O(1)')
print(brute_force(nums))
print('Time Taken:', (time()-s1))