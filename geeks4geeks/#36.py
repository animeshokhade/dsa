# question --> https://practice.geeksforgeeks.org/problems/display-longest-name0853/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def longest(self, names, n):
        # code here
        maxString = names[0]
        for index in range(1, n):
            if len(names[index]) > len(maxString):
                maxString = names[index]
        return maxString

    # TC: O(N); SC: O(1)
# end
