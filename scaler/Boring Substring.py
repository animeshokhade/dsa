class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        max_odd = '!'
        max_even = '!'

        min_odd = '~'
        min_even = '~'

        for ch in A: 
            if ord(ch) & 1: 
                max_odd = max(max_odd, ch)
                min_odd = min(min_odd, ch)
            else:
                min_even = min(min_even, ch)
                max_even = max(max_even, ch) 

        if ord(max_odd) - ord(min_even) > 1:
            return 1

        if ord(max_even) - ord(min_odd) > 1: 
            return 1

        return 0 

        # TC: O(N); SC: O(1)