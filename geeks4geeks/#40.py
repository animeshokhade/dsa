# question --> https://practice.geeksforgeeks.org/problems/java-reverse-a-string0416/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def revStr(ob, S):
        # code here
        ans = ''
        for char in reversed(S):
            ans += char
        return ans

    # TC: O(|S|); SC: O(|S)
# end
