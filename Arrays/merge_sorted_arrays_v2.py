''' 
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
'''
from time import time
import random

nums1 = sorted([random.randint(1, 500) for i in range(20000)]) + [0]*20000
m = 20000
nums2 = sorted([random.randint(1, 500) for i in range(20000)])
n = 20000

def brute_force(arr1, m, arr2, n):
	'''
	Brute force solution O((m+n)log(m+n))
	'''
	#sorted function has the time complexity on nlog(n)
	arr1[m:] = arr2
	arr1.sort()
	return arr1

def optimized_soln(arr1, m, arr2, n):
	'''
	Optimized Soltution O(m+n)
	'''
	nums1_c = arr1[:m]
	p1 = 0
	p2 = 0
    
	for i in range(n+m):
		if (p1<m and nums1_c[p1] <= arr2[p2]) or p2>n:
			arr1[i] = nums1_c[p1]
			p1 = p1+1
		else:
			arr1[i] = arr2[p2]
			p2 = p2 + 1
	return arr1


s1 = time()
print('Brute Force: O((m+n)log(m+n)),  Space complexity O(1)')
brute_force(nums1,m,nums2,n)
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: Time Complexity O(m+n),  Space complexity O(m)')
optimized_soln(nums1,m,nums2,n)
print('Time Taken: ',(time()-s2))
