# question --> https://practice.geeksforgeeks.org/problems/second-largest3735/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:

	def print2largest(self,arr, n):
		# code here
		Max = max(arr)
		ans = float('-inf')
		for a in arr:
		    if a != Max:
		        ans = max(ans, a)
		if ans == float('-inf'): return -1
		return ans

        # TC: O(N); SC: O(1)
# end 