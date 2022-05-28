class Solution:
	# @param A : list of integers
	# @return a list of integers
	def lszero(self, A):
        PS = dict()
        ans = list()
        summ = 0
        base = -1
        for index, num in enumerate(A):
            summ += num
            if summ in PS:
                if index - PS[summ] > base:
                    base = index - PS[summ]
                    ans = A[PS[summ] + 1:index + 1]
            elif summ == 0:
                if index + 1 > base:
                    base = index + 1
                    ans = A[:index + 1]
            else:
                PS[summ] = index
        return ans

# alternative approach

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        PS = dict()
        ans = list()
        summ = 0
        cmpp = -1
        for index, num in enumerate(A):
            summ += num
            if summ in PS:
                if index - PS[summ] > cmpp:
                    cmpp = index - PS[summ]
                    ans = A[PS[summ] + 1:index + 1]
            elif summ == 0:
                if index + 1 > cmpp:
                    cmpp = index + 1
                    ans = A[:index + 1]
                elif index + 1 == cmpp:
                    pass
            else:
                PS[summ] = index
        return ans

    


