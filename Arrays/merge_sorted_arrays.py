''' Merge sorted arrays'''
from time import time
import random

array1 = sorted([random.randint(1, 500) for i in range(100000)])
array2 = sorted([random.randint(1, 1000000) for i in range(100000)])

def brute_force(arr1, arr2):
	'''
	Brute force solution O((n1+n2)log(n1+n2)),  Space complexity O(1)

	'''
	#sorted function has the time complexity on nlog(n)
	return sorted(arr1+arr2)


def optimized_soln(arr1, arr2):
	'''
	More optimized soltuion Time Complexity O(n1+n2),  Space complexity O(n1+n2) 

	'''
	i = 0
	j = 0
	merged_array = []
	s1 = time()
	#if one of the arrays is empty , no need to merge
	if len(arr1) == 0:
		return arr2

	if len(arr2) ==0:
		return arr1

	while i<len(arr1):
		if arr1[i] <= arr2[j]:
			if i < (len(arr1) - 1):
				merged_array.append(arr1[i])
				i = i + 1
			else:
				merged_array.append(arr1[i])
				merged_array = merged_array + arr2[j:]
				i = len(arr1)
		else:
			if j < (len(arr2) - 1):
				merged_array.append(arr2[j])
				j = j + 1
			else:
				merged_array.append(arr2[j])
				merged_array = merged_array + arr1[i:]
				i = len(arr1)

	return merged_array

#Logically the optimized solution is better. But according to my intuition the brute force sorting is working faster because most part of the array is already sorted
#Timsort is used by python's sorted() function which perofrms O(n) in best case scenario and doesn't require extra append functions like our optimized solution needs
#Thus seems to be making the brute force solution almost 10X faster than out optimized solution

s1 = time()
print('Brute Force: O((n1+n2)log(n1+n2)),  Space complexity O(1)')
brute_force(array1,array2)
print('Time Taken: ',(time()-s1))
s2 = time()
print('Optimized Soln: Time Complexity O(n1+n2),  Space complexity O(n1+n2)')
optimized_soln(array1,array2)
print('Time Taken: ',(time()-s2))