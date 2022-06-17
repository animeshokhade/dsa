class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        string = list(str(A))
        n = len(string)
        set_size = (n * (n + 1)) // 2
        product = set()
        for i in range(n):
            j = i
            while j < n:
                if i == j:
                    product.add(int(string[j]))
                else:
                    temp = 1
                    for k in range(i, j + 1):
                        temp *= int(string[k])
                    product.add(temp)
                j += 1

        if set_size != len(product):
            return 0
        return 1


# optimisation

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):

        # creating the digits array
        digits = []
        while A:
            digits.append(A % 10)
            A //= 10

        # reversing to restore the original digits order
        digits = digits[::-1]

        lkp = set()
        n = len(digits)

        # multiply every element with every other element
        for i in range(n):
            p = 1
            for j in range(i, n):
                p *= digits[j]
                if p in lkp:
                    return 0
                lkp.add(p)
        return 1

    # TC: O(N^2); SC: O(N)
