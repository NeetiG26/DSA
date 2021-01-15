''' Merge sorted arrays'''
from time import time

array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]


def brute_force(arr1, arr2):
	'''
	Brute force solution 

	'''
	i = 0
	j = 0
	merged_array = []
	s1 = time()
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


	print('Brute Force: O(n1+n2) solution')
	print('Time Taken: ',(time()-s1))
	return merged_array

print(brute_force(array1, array2))