# question --> https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        ret = '0'
        sign = 1

        if s[0] in {'-', '+'}:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        for ch in s:
            if ch.isdigit():
                ret += ch
            else:
                break

        lo = -pow(2, 31)
        hi = -lo - 1

        ret = int(ret)
        ret *= sign
        if ret < lo:
            ret = lo
        elif ret > hi:
            ret = hi
        return ret

    # TC: O(|S|); SC: O(|S|)

# optimised

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        ret = 0
        sign = 1

        if s[0] in {'-', '+'}:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        for ch in s:
            if ch.isdigit():
                ret = ret * 10 + ord(ch) - ord('0')
            else:
                break

        lo = -pow(2, 31)
        hi = -lo - 1

        ret *= sign
        if ret < lo:
            ret = lo
        elif ret > hi:
            ret = hi
        return ret

        # TC: O(N); SC: O(1)