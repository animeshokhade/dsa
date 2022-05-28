class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lst = list(A)
        test = dict()

        for char in lst:
            if char in test:
                test[char] += 1
            else:
                test[char] = 1

        t = sorted(test.items(), key=lambda x: x[1])
        i = B
        while i > 0:
            if t[0][1] <= i:
                i -= t[0][1]
                t.pop(0)
            else:
                break

        return len(t)

# alternative approach

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lst = list(A)
        test = dict()

        for char in lst:
            if char in test:
                test[char] += 1
            else:
                test[char] = 1

        t = sorted(test.items(), key=lambda x: x[1])
        i = B
        while i > 0:
            if t[0][1] <= i:
                i -= t[0][1]
                t.pop(0)
            else:
                break

        return len(t)

# alterative approach

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lst = list(A)
        test = dict()

        for char in lst:
            if char in test:
                test[char] += 1
            else:
                test[char] = 1

        t = sorted(test.items(), key=lambda x: x[1])
        i = B
        while i > 0:
            if t[0][1] <= i:
                i -= t[0][1]
                t.pop(0)
            else:
                i = 0

        return len(t)

# alternative approach

class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        lst = list(A)
        test = dict()

        for char in lst:
            if char in test:
                test[char] += 1
            else:
                test[char] = 1

        for b in range(B):
            min_value = min(test.values())
            key = [k for k in test if test[k] == min_value]
            test[key[0]] -= 1
            if test[key[0]] == 0:
                del test[key[0]]

        return len(test)
