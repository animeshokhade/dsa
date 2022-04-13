# question --> https://practice.geeksforgeeks.org/problems/value-equal-to-index-value1330/1/?page=1&difficulty[]=-2&status[]=unsolved&category[]=Arrays&sortBy=submissions

class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		ans = list()
		for index, num in enumerate(arr):
		    if num == index + 1:
		        ans.append(num)
		return ans

        # TC: O(N); SC: O(N)