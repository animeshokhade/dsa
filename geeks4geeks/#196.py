# question --> https://practice.geeksforgeeks.org/problems/searching-a-number0324/1/?page=2&difficulty[]=-1&status[]=unsolved&sortBy=submissions

class Solution:

	
	def search(self,arr, n, k): 
    	# code here
    	if k not in arr: return -1
    	return arr.index(k) + 1

    # TC: O(N); SC: O(1)