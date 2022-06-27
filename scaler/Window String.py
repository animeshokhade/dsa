from collections import Counter

class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def minWindow(self, A, B):
        freq = Counter(B)
        
        # idea is to track the required number of 
        # characters and their minimum frequency 
        req = len(B)

        # we have to return the smallest possible window string 
        # and in case of equal length substrings - window string with smaller index 
        min_left = float('inf')
        min_len = float('inf')

        l = 0
        for r, c in enumerate(A):
            # req is initalised to len(B), meaning it takes all the characters
            # and their frequency count 

            # as we traverse A, we reduce the count of each character in 
            # freq. If after processing a character count, we find that the 
            # count of that character is non-negative, that means it is a 
            # character which is present in B and hence we update the req 
            # as we have now found this particular character and thus, require 
            # 1 less character to match B in A  
            freq[c] -= 1
            if freq[c] >= 0: 
                req -= 1

            # when req == 0, it means that we have found the required window string 
            # but, now the task is to fetch the minimum size window sub-string and so,
            # we move the l pointer forward while updating min_left and min_len.  
            while req == 0: 
                if r - l + 1 < min_len: 
                    min_left = l 
                    min_len = r - l + 1

                # Since we were decrementing the freq count when processing characters
                # when the r pointer was moving, now the counts are incremented as the 
                # l pointer moves which is reflected in the min_left and min_right in the
                # next iteration. 
                freq[A[l]] += 1

                # when the right pointer moves, it decrements and so the characters 
                # in B which are found in A move towards 0. Once the right pointer stops
                # then the characters in B are all found in A, and their freq count is 
                # either 0 or negative. So, when the left pointer moves, it starts to 
                # increment freq count and so, if the freq count goes above 0 for a 
                # character, that means it must be a character in B, because these are 
                # the only ones which had positive counts before the for loop ran.
                # So, every other character at max can have a 0 count when the left 
                # pointer increments frequency. So, when the count of a character goes 
                # above 0, it means that we have a lost a character which was in B and 
                # had been found in A, and so now we increment req as we need that character 
                if freq[A[l]] > 0: 
                    req += 1

                l += 1

        # if the while loop is never processed, then we never update min_left and 
        # it implies that the characters in B can't be found in A 
        return '' if min_left == float('inf') else A[min_left:min_left + min_len]

        # TC: O(A); SC: O(128 ~ 1)