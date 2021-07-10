# Two pointer technique based solution to find
# if there is a pair in A[0..N-1] with a given sum.
def isPairSum(A, N, X):

	# represents first pointer
	i = 0

	# represents second pointer
	j = N - 1

	while(i < j):
	
		# If we find a pair
		if (A[i] + A[j] == X):
			return True

		# If sum of elements at current
		# pointers is less, we move towards
		# higher values by doing i += 1
		elif(A[i] + A[j] < X):
			i += 1

		# If sum of elements at current
		# pointers is more, we move towards
		# lower values by doing j -= 1
		else:
			j -= 1
	return 0

# array declaration
arr = [3, 5, 9, 2, 8, 10, 11]

# value to search
val = 17

print(isPairSum(arr, len(arr), val))

# This code is contributed by maheshwaripiyush9.
