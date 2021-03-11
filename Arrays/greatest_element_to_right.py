'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
'''

from time import time
import random

nums = [random.randint(1,5000) for i in range(1000)]

def brute_force(arr):
	'''
	Brute Force Solution on TC O(n^2) and SC O(n)
	'''
	if len(arr) == 1:
		return [-1]

	for i in range(len(arr)-1): #O(n)
		arr[i] = (max(arr[i+1:])) #O(n)
	arr[-1]=(-1)
	return arr

def optimized_soln(arr):
	'''
	More optimized soltuion Time Complexity O(n), Space Complexity O(n)

	'''
	out = [-1]
	greatest = 0

	for num in arr[::-1]:
		if greatest < num:
			greatest = num
		out.append(greatest)
	out.pop()
	return out[::-1]


s1 = time()
print('Brute Force: O(n) solution, Space complexity O(n)')
brute_force(nums)
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: O(n) solution, O(n) Space complexity')
optimized_soln(nums)
print('Time Taken: ',(time()-s2))