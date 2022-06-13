# question --> https://practice.geeksforgeeks.org/problems/find-the-camel3348/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def countCamelCase(self, s):
        # your code here
        ans = 0
        for index in range(len(s)):
            if s[index].isupper():
                ans += 1
        return ans

        # TC: O(|S|); SC: O(1)

    