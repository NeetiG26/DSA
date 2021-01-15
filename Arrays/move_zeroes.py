''' Given an array nums, write a function to move all 0's to the end of it inplace, without making a copy of the array 
and while maintaining the relative order of the non-zero elements '''
from time import time

nums_l = [0,13,5,20,0,31,50,20,2,7,0,11,15,0]

def brute_force(nums):
	'''
	Brute force solution (O(n^2))

	'''
	for i in range(len(nums)):
		if nums[i] == 0:
			nums.remove(0) # O(n)
			nums.append(0) # O(1)
	return nums




def optimized_soln(nums):
	'''
	More optimized soltuion (O(n))

	'''
	pos = 0
        
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[pos], nums[i] = nums[i], nums[pos] #(O(1))
			pos += 1
	return nums


s1 = time()
print('Brute Force: O(n^2) solution')
print(brute_force(nums_l))
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: O(n) solution')
print(optimized_soln(nums_l))
print('Time Taken: ',(time()-s2))
