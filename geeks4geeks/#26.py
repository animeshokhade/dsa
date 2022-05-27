# question --> https://practice.geeksforgeeks.org/problems/find-the-median0527/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def find_median(self, v):
        # Code here
        v.sort()
        if len(v) & 1: return v[len(v) // 2]
        return (v[len(v) // 2] + v[len(v) // 2 - 1]) // 2

    # TC: O(NlogN); SC: O(1)
# end
