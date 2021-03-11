''' Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M). '''
from time import time
import random

nums = [random.randint(1,5000) for i in range(10000)]

def brute_force(arr):
	'''
	Brute Force Solution on TC O(n^2) and SC O(1)
	'''
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if (arr[i] == 2*arr[j]) or (arr[j] == 2*arr[i]):
				return True
	return False


def optimized_soln(arr):
	'''
	More optimized soltuion Time Complexity O(n), Space Complexity O(n)

	'''
	seen = set()
	for i in arr:
	# if 2 * i in seen or i % 2 == 0 and i // 2 in seen:
		if 2 * i in seen or i / 2 in seen: 
			return True
		seen.add(i)
	return False


s1 = time()
print('Brute Force: O(n^2) solution, Space complexity O(1)')
print(brute_force(nums))
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: O(n) solution, O(n) Space complexity')
print(optimized_soln(nums))
print('Time Taken: ',(time()-s2))