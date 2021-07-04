''' 
Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

from time import time 
import random

array1 = [random.randint(1, 500) for i in range(100000)]

def brute_force(nums):
    one_time = set()
    more_times = set()
    
    for ele in nums:
        if ele not in more_times:
            if ele in one_time:
                more_times.add(ele)
            else:
                one_time.add(ele)
    return (list(one_time-more_times))[0]

def optimized_soln(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()



s1 = time()
print('Brute Force: O(n),  Space complexity O(n)')
brute_force(array1)
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: Time Complexity O(n),  Space complexity O(n)')
optimized_soln(array1)
print('Time Taken: ',(time()-s2))