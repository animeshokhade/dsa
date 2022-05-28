class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 1 if A % 9 == 1 else 0
        return ans

# alternative approach

def summ(A):
    if A // 10 == 0:
        return A % 10
    return summ(A // 10) + A % 10

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if summ(A) == 1:
            return 1
        elif summ(A) > 9:
            return self.solve(summ(A))
        return 0

# alternate approach

class Solution:
    # @param A : integer
    # @return an integer
    def add(self, A):
        if A == 0:
            return 0
        return A % 10 + self.add(A // 10)

    def solve(self, A):
        ans = self.add(A)
        while ans > 9:
            ans = self.add(ans)
        else:
            if ans == 1:
                return 1
            else:
                return 0



