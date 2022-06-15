class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        ans = set()
        n = len(A)
        p1 = 0
        p2 = 1
        A.sort()

        while p2 < n:
            diff = A[p2] - A[p1]
            if diff == B:
                ans.add(tuple([A[p1], A[p2]]))
                p1 += 1
                p2 += 1
            elif diff > B:
                p1 += 1
                if p1 == p2:
                    p2 += 1
            else:
                p2 += 1

        return len(ans)

    # TC: O(NlogN); SC: O(N^2)


# optimisation

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        freq = {}
        p = 0

        # hashing for arrays with unique elements
        if B != 0:
            for a in set(A):
                if a in freq:
                    freq[a] += 1
                if a not in freq:
                    freq[a] = 1
                if a + B in freq:
                    p += 1
                if a - B in freq:
                    p += 1

        # hashing for arrays with duplicates
        else:
            for a in A:
                if a in freq:
                    freq[a] += 1
                else:
                    freq[a] = 1
            for f in freq:
                if freq[f] > 1:
                    p += 1

        return p

        # TC: O(N); SC: O(N)


# optimisation

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        p1 = 0
        p2 = 1
        pairs = 0
        A.sort()

        while p2 < n:
            diff = A[p2] - A[p1]
            if diff == B:
                pairs += 1
                p1 += 1
                p2 += 1

                # handling duplicates
                while p2 < n and A[p2] == A[p2 - 1]:
                    p2 += 1
                while p1 < p2 and p1 > 0 and A[p1] == A[p1 - 1]:
                    p1 += 1

            elif diff > B:
                p1 += 1
                if p1 == p2:
                    p2 += 1
            else:
                p2 += 1

        return pairs

        # TC: O(NlogN); SC: O(1)    
