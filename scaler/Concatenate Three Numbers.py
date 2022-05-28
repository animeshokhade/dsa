class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        array = [A, B, C]
        temp = sorted(array)
        string = [str(i) for i in temp]
        ans = ''.join(string)
        return ans

    