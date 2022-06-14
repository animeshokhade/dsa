# question --> https://practice.geeksforgeeks.org/problems/triangle-shrinking-downwards0459/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions

class Solution:
    def triDownwards(self, S):
        # code here
        for s in range(len(S)):
            print('.' * s + S[s:])
        return ''

    # TC: O(|S|); SC: O(1)
