# question --> https://practice.geeksforgeeks.org/problems/sum-palindrome3857/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def isPalindrome(self, is_pal):
        l, r = 0, len(is_pal) - 1
        while l < r:
            if is_pal[l] != is_pal[r]:
                return 0
            l += 1
            r -= 1
        return 1

    def isSumPalindrome(self, n):
        # code here
        i = 0
        pal = self.isPalindrome(str(n))
        if pal: return n
        while i < 5 and pal == False:
            i += 1
            is_pal = str(n + int(str(n)[::-1]))
            pal = self.isPalindrome(is_pal)
            if pal:
                return int(is_pal)
            n = int(is_pal)
        return -1

    # TC: O(|S|); SC: O(1)