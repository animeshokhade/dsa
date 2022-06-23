# question --> https://practice.geeksforgeeks.org/problems/print-first-letter-of-every-word-in-the-string3632/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions

class Solution:
	def firstAlphabet(self, S):
		# code here
		S = list(S.split())
		for word in S: 
		    print(word[0], sep='', end = '')
		return ''
		
	# TC: O(|S|); SC: O(|S|)