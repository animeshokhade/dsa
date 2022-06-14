# question --> https://practice.geeksforgeeks.org/problems/reversing-the-vowels5304/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def modify(self, s):
        # code here
        l, r = 0, len(s) - 1
        s = list(s)
        vow = {'a', 'e', 'i', 'o', 'u'}
        while l < r:
            if s[l] not in vow:
                l += 1
            elif s[r] not in vow:
                r -= 1
            else:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)

        # TC: O(|S|); SC: O(1)
