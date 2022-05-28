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

