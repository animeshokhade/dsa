# question --> https://practice.geeksforgeeks.org/problems/subset-sums2234/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
	def subsetSums(self, arr, N):
		# code here
		sub = (1 << N)
		sub_sum = [0] * sub
		
		for bit in range(sub):
		    cur_sum = 0
		    ind = 0
		    seq = bit
		    while seq: 
		        if seq & 1: 
		            cur_sum += arr[N - ind - 1]
		        ind += 1
		        seq >>= 1
		    sub_sum[bit] = cur_sum 
		    
		return sub_sum
		
		# TC: O(2^N); SC: O(2^N)