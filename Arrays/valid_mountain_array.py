'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
'''
from time import time
import random

nums = [random.randint(1,5000) for i in range(100)]

def brute_force(arr):
    # print(arr)
    for i in range(len(arr)-1):
        arr[i] = arr[i] - arr[i+1]
    # print(arr) 
    # arr[-1] = 1
    change_sign = 0
    last_sign = 'neg'
    
    if arr[0] >= 0:
        return False
    
    
    for i in range(len(arr)-1):
        if arr[i] > 0:
            current_sign = 'pos'
        elif arr[i] < 0:
            current_sign = 'neg'
        else:
            return False

        
        if current_sign != last_sign:
            if i == 0:
                return False
            else:
                last_sign = current_sign
                change_sign = change_sign + 1
    
    if change_sign == 1:
        return True
    else:
        return False


def simpler_soln(arr):
    i = 0
    n = len(arr)
    
    while (i+1 < n) and (arr[i] < arr[i+1]):
        i = i+1
    
    if (i==0) or (i==n-1):
        return False
    
    while (i+1 <n) and (arr[i] > arr[i+1]):
        i = i+1
        
    return (i == n-1)


s1 = time()
print('Brute Force: O(n) solution, Space complexity O(1)')
print(brute_force(nums))
print('Time Taken: ',(time()-s1))
s2 = time()
print('Simpler Soln: O(n) solution, O(1) Space complexity')
print(simpler_soln(nums))
print('Time Taken: ',(time()-s2))
