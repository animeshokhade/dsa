class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        even, odd = 0, 1
        beginsEven, beginsOdd = 0, 0

        for a in A:
            if a & 1 == even:
                beginsEven += 1
                even ^= 1

            if a & 1 == odd:
                beginsOdd += 1
                odd ^= 1

        return max(beginsEven, beginsOdd)

# alternative approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        ans1, ans2 = 0, 0
        x, y = 1, 0

        for it in A:
            it = (it & 1)
            if (it == x):
                ans1 += 1
                x ^= 1

            if (it == y):
                y ^= 1;
                ans2 += 1

        return max(ans1, ans2)

# alternative approach

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        switch = A[0] % 2
        beginsEven, beginsOdd = 1, 1
        if switch:
            for index in range(1, len(A)):
                switch = A[index] % 2
                if switch:
                    if beginsOdd & 1 == 0:
                        beginsOdd += 1
                else:
                    if beginsOdd & 1 == 1:
                        beginsOdd += 1

        else:
            for index in range(1, len(A)):
                switch = A[index] % 2
                if not switch:
                    if beginsEven & 1 == 0:
                        beginsEven += 1
                else:
                    if beginsEven & 1 == 1:
                        beginsEven += 1

        return max(beginsEven, beginsOdd)

