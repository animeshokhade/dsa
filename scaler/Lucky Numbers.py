class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        lucky = 0
        divisors = [0] * (A + 1)
        prime = 2
        while prime <= A:
            # lucky increment
            if divisors[prime] == 2:
                lucky += 1

            # 0 indicates a new prime number
            if divisors[prime] == 0:
                for i in range(2 * prime, A + 1, prime):
                    divisors[i] += 1
            prime += 1

        return lucky


'''
TC: O(NlogN)
The reason we were visiting the subsequent elements in a sieve starting from 
i^2 was because we didn't want to revisit the previously marked off elements.
However, in this case we have to revisit every number starting from 2i because
we want to count its distinct prime factors. Hence in this case the second
log won't come as the i^2 jump won't happen. 
'''

# alternate approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        lucky = 0
        divisors = [0] * (A + 1)
        prime = 2
        while prime <= A:
            # lucky increment
            if divisors[prime] == 2:
                lucky += 1
                prime += 1
                continue

                # 0 indicates a new prime number
            if divisors[prime] == 0:
                for i in range(2 * prime, A + 1, prime):
                    divisors[i] += 1
            prime += 1

        return lucky

# alternate approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # int sieve
        spf = [0] * (A + 1)
        for i in range(A + 1):
            spf[i] = i

        j = 2
        while j * j <= A:
            if spf[j] == j:
                # prime number
                k = j * j
                while k <= A:
                    if spf[k] == k:
                        spf[k] = j
                    k += j
            j += 1

        # lucky numbers
        lucky = 0
        i = 2
        while i <= A:
            divisors = 0
            j = i
            while j > 1:
                p = spf[j]
                while j % p == 0:
                    j //= p
                divisors += 1
            if divisors == 2:
                lucky += 1
            i += 1

        return lucky

# alternate approach

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        # int sieve
        spf = [0] * (A + 1)
        for i in range(A + 1):
            spf[i] = i

        j = 2
        while j * j <= A:
            if spf[j] == j:
                # prime number
                k = j * j
                while k <= A:
                    if spf[k] == k:
                        spf[k] = j
                    k += j
            j += 1

        # lucky numbers
        lucky = 0
        i = 2
        while i <= A:
            divisors = 0
            j = i
            while j > 1:
                flag = False
                p = spf[j]
                while j % p == 0:
                    j //= p
                    flag = True
                if flag:
                    divisors += 1
            if divisors == 2:
                lucky += 1
            i += 1

        return lucky

