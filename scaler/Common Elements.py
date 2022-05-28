class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        if len(A) <= len(B):
            flag = True
            mapA = dict()
            for num in A:
                if mapA.get(num) == None:
                    mapA[num] = 1
                else:
                    mapA[num] += 1

        else:
            flag = False
            mapB = dict()
            for num in B:
                if mapB.get(num) == None:
                    mapB[num] = 1
                else:
                    mapB[num] += 1

        ans = list()
        if flag:
            for num in B:
                if mapA.get(num) != None and mapA[num] != 0:
                    ans.append(num)
                    mapA[num] -= 1

        else:
            for num in A:
                if mapB.get(num) != None and mapB[num] != 0:
                    ans.append(num)
                    mapB[num] -= 1

        return ans

# alternative approach

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        mapA = dict()
        mapB = dict()

        for num in A:
            if num in mapA:
                mapA[num] += 1
            else:
                mapA[num] = 1

        for num in B:
            if num in mapB:
                mapB[num] += 1
            else:
                mapB[num] = 1

        ans = list()

        for key in mapA:
            if key in mapB:
                ans += min(mapA[key], mapB[key]) * [key]

        return ans