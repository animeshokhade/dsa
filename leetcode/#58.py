# question --> https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)

        ret = 0
        for i in range(n - 1, -1, -1):
            if s[i] == ' ':
                break
            ret += 1

        return ret

    # TC: O(|S|); SC: O(1)
    