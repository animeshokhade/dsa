class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        if all(A):
            return 0
        switch = 0
        bulb = False
        for state in A:
            if not bulb:
                if state == 0:
                    switch += 1
                    bulb = True
            elif bulb:
                if state == 1:
                    switch += 1
                    bulb = False

        return switch

