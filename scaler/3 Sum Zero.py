class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        vec = []
        n = len(A)
        if n == 0: return vec  # handling empty array
        a = 0
        while a < n - 2:
            # avoiding duplicates
            if a > 0 and A[a] == A[a - 1]:
                a += 1
                continue
            b = a + 1
            c = n - 1
            sum_req = -A[a]
            while b < c:
                cur_sum = A[b] + A[c]
                if cur_sum > sum_req:
                    c -= 1
                elif cur_sum < sum_req:
                    b += 1
                else:
                    vec.append([A[a], A[b], A[c]])
                    # avoiding duplicates
                    b += 1
                    while b < c and A[b] == A[b - 1]:
                        b += 1
            a += 1
        return vec

    # TC: O(N^2); SC: O(1)

# clean

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        vec = []
        n = len(A)
        if n == 0: return vec  # handling empty array
        for a in range(n - 2):
            # avoiding duplicates
            if a == 0 or A[a] != A[a - 1]:
                b = a + 1
                c = n - 1
                while b < c:
                    sum_req = A[a] + A[b] + A[c]
                    if sum_req == 0:
                        vec.append([A[a], A[b], A[c]])
                        # avoiding duplicates
                        b += 1
                        while b < c and A[b] == A[b - 1]:
                            b += 1
                        c -= 1
                        while b < c and A[c] == A[c + 1]:
                            c -= 1
            elif sum_req > 0:
                c -= 1
            else:
                b += 1

        return vec

    # TC: O(N^2); SC: O(1)
