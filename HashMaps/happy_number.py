'''
Happy Number 

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.
'''

from time import time

def brute_force(n: int) -> bool:
    values = set()
    
    for i in range(100):
        # digits = str(n).split('')
        # print(digits)
        val = 0
        for ele in str(n):
            # print(ele)
            val = val + (int(ele))**2
        # print(val)
            
        if val == 1:
            return True                
        elif val not in values:
            values.add(val)
            n = val
        else:
            return False

s1 = time()
print('Brute Force: O(log(n)),  Space complexity O(1)')
brute_force(19)
print('Time Taken: ',(time()-s1))