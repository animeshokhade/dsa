class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        lkp = set()
        l, r = 0, 0
        n = len(A)

        sub = 0

        while r < n: 
            if A[r] not in lkp: 
                lkp.add(A[r])
                r += 1
            else: 
                lkp.remove(A[l])
                l += 1 
            sub = max(sub, r - l)

        return sub 

        # TC: O(N); SC: O(N) 

# alternate approach

class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        lkp = {}
        l, r = 0, 0
        n = len(A)

        sub = 0

        for r in range(n): 
            if A[r] in lkp and l <= lkp[A[r]]: 
                l = lkp[A[r]] + 1
            else: 
                sub = max(sub, r - l + 1)
            lkp[A[r]] = r 

        return sub 

        # TC: O(N); SC: O(N) 
