# question --> https://practice.geeksforgeeks.org/problems/remove-spaces0128/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def modify(self, s):
        # code here
        return ''.join(list(s.split()))

    # TC: O(N); SC: O(1)
# end
