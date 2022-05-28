class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        lst = list(str(A))
        test = dict()
        for char in lst:
            if char in test:
                test[char] += 1
            else:
                test[char] = 1

        count = 0
        for key in test:
            if test[key] & 1 != 0:
                count += 1

        if count > 1:
            return 0
        return 1

# alternative approach

