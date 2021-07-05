'''
Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
'''
from time import time
import random

array1 = sorted([random.randint(1, 500) for i in range(100000)])
array2 = sorted([random.randint(1, 1000000) for i in range(100000)])

def brute_force(nums1, nums2):
    set1 = set(nums1) - set(nums2)
    set2 = set(nums2) - set(nums1)
    
    return ((set(nums1) - set1) - set2)


s1 = time()
print('Brute Force: O(n),  Space complexity O(n)')
brute_force(array1,array2)
print('Time Taken: ',(time()-s1))
