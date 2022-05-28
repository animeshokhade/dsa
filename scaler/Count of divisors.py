class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # sieve
        maxA = max(A)

        spf = [0] * (maxA + 1)
        for i in range(maxA + 1):
            spf[i] = i

        j = 2
        while j * j <= maxA:
            if spf[j] == j:
                # number is prime
                k = j * j
                while k <= maxA:
                    if spf[k] == k:
                        spf[k] = j
                    k += j
            j += 1

        # counting divisors
        ans = []
        for a in A:
            divisorCount = 1
            while a > 1:
                p = spf[a]
                power = 0
                while a % p == 0:
                    power += 1
                    a //= p
                divisorCount *= power + 1
            ans.append(divisorCount)

        return ans

'''
TC: O(NloglogN) + O(QlogN)
QlogN dominates so, TC: O(QlogN) 
Q --> Querries
N is required to create the sieve array.
logN is due to iterative/recursive division. The worst case would be division by 2.
As the largest number of iterations would happen for repeated divisions by the 
smallest prime number i.e. 2. So the base of the log in this TC is 2. 
'''

# alternate approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        maxA, p = max(A), 2
        # storing prime factors of numbers from 1 --> maxA

        prime = [-1] * (maxA + 1)
        while p * p <= maxA:
            if prime[p] == -1:
                prime[p] = p
                for i in range(p * p, maxA + 1, p):
                    if prime[i] == -1:
                        prime[i] = p
            p += 1

        ans = []

        # number of divisors for every integer
        for a in A:
            if a == 1:
                ans.append(1)
                continue

            num, divisorCount = a, 1
            while num > 1:
                count = 0
                temp = prime[num]
                while num > 1 and num % temp == 0:
                    num //= temp
                    count += 1
                divisorCount *= (count + 1)
            ans.append(divisorCount)
        return ans

# alternate approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        mx, p = max(A), 2
        prime = [-1] * (mx + 1) #Stores the smallest prime factor of integers 1 to max(A)
        while p * p <= mx:
            if prime[p] == -1:
                prime[p] = p
                for i in range(p * p, mx + 1, p):
                    if prime[i] == -1:
                        prime[i] = p
            p += 1
        ans = []
        #Using prime factorization to get the number of divisors for every integer
        for i in A:
            if i == 1:
                ans.append(1)
                continue
            num, num_of_divisors = i, 1
            while num > 1:
                cnt = 0
                temp = prime[num]
                while num > 1 and num % temp == 0:
                    num //= temp
                    cnt += 1
                num_of_divisors *= (cnt + 1)
            ans.append(num_of_divisors)
        return ans

