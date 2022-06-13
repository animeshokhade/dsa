# question --> https://practice.geeksforgeeks.org/problems/java-delete-alternate-characters4036/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def delAlternate(ob, S):
        # code here
        S = list(S)
        n = len(S)
        for index in range(1, n, 2):
            S[index] = ''
        return ''.join(S)

    # TC: O(|S|); SC: O(|S|)
