# question --> https://practice.geeksforgeeks.org/problems/odd-or-even3618/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def oddEven (ob,N):
        # code here
        if N & 1: return 'odd'
        return 'even'

    # TC: O(1); SC: O(1)
# end