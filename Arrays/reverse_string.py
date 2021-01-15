''' Reverse a string '''
from time import time

var = 'Hi! My name is Neeti'

def brute_force(val):
	'''
	Brute force solution 

	'''
	s1 = time()
	out = ''
	if type(val) == str:
		for i in range(len(val)):
			out = out+val[(len(val)-1)-i]
	else:
		out = 'Invalid Input'

	print('Brute Force: O(n) solution')
	print(out)
	print('Time Taken: ',(time()-s1))
	return


brute_force(var)