class Solution:
	# @param A : string
	# @return an integer
	def titleToNumber(self, A):
        index = ['A',
                 'B',
                 'C',
                 'D',
                 'E',
                 'F',
                 'G',
                 'H',
                 'I',
                 'J',
                 'K',
                 'L',
                 'M',
                 'N',
                 'O',
                 'P',
                 'Q',
                 'R',
                 'S',
                 'T',
                 'U',
                 'V',
                 'W',
                 'X',
                 'Y',
                 'Z']

        summ, i = 0, 0
        for string in A:
            position = index.index(string)
            weight = position + 1
            summ += weight * (26 ** (len(A) - 1 - i))
            i += 1

        return summ


