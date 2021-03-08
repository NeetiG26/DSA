'''Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.'''
from time import time
import random

nums_l = [random.randint(0, 10) for i in range(1000)]

def brute_force(arr):
    """
    Brute Force Solution : O(n^n)
    """
    i = 0
    
    while i < (len(arr)):
        if arr[i] == 0 :
            temp = 0
            i = i+1
            
            for j in range(i, len(arr)):
                temp, arr[j]= arr[j], temp
                
        i = i+1
    return arr

def optimized_soln(arr):
	"""
	Better Solution
	"""
	i = 0
	while i < len(arr):
		if arr[i] == 0:
			arr.insert(i+1,0)
			arr.pop()
			i = i+1
		i = i + 1
	return arr



s1 = time()
print('Brute Force')
brute_force(nums_l)
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Solution')
optimized_soln(nums_l)
print('Time Taken: ', (time()-s2))
