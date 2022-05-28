class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        r = [[]]
        for e in A:
            r += [x + [e] for x in r]
        return sorted(r)

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        n = len(A)
        bitMapCount = 1 << n

        ans = [[]]

        for bitRep in range(1, bitMapCount):
            subSet = []
            bitTracker = 0
            while bitRep:
                if bitRep & 1:
                    subSet.append(A[bitTracker])
                bitRep >>= 1
                bitTracker += 1
            ans.append(sorted(subSet))

        return sorted(ans)




