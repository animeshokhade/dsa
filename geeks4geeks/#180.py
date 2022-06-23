# question --> https://practice.geeksforgeeks.org/problems/number-of-occurrence2259/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

from bisect import bisect_left, bisect_right
class Solution:

	def count(self,arr, n, x):
		# code here
		l = bisect_left(arr, x)
		r = bisect_right(arr, x)
		return r - l
		
	# TC: O(logN); SC: O(1)