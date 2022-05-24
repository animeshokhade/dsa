# question --> https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1/?page=1&difficulty[]=0&status[]=unsolved&category[]=Arrays&category[]=Strings&sortBy=submissions#

class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	lookup = set()
    	ans = set()
    	for i in range(n):
    	    if arr[i] in lookup: 
    	        ans.add(arr[i])
    	    else: 
    	        lookup.add(arr[i])
    	if ans: 
    	    return sorted(list(ans)) 
    	return [-1]

# TC: O(N); SC: O(N)
# end 