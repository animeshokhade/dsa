# question --> https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None:
            return 0

        return haystack.find(needle)

    # TC: O(|S|); SC: O(1) 