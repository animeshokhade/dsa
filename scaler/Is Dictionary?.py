class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        sort_order = dict()
        for index, char in enumerate(B):
            sort_order[char] = index

        iterations = len(A) - 1
        for index in range(iterations):
            flag = 0
            string_left = A[index]
            string_right = A[index + 1]
            repetitions = min(len(string_left), len(string_right))
            for index in range(repetitions):
                if sort_order[string_left[index]] != sort_order[string_right[index]]:
                    if sort_order[string_left[index]] > sort_order[string_right[index]]:
                        return 0
                    flag = 1
                    break

            if not flag:
                if len(string_left) > len(string_right):
                    return 0

        return 1

# alternative approach

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        sort_order = dict()
        for index, char in enumerate(B):
            sort_order[char] = index

        for index in range(len(A)):
            if index == len(A) - 1:
                break
            iterations = min(len(A[index]), len(A[index + 1]))
            i = 0
            string_left = A[index]
            string_right = A[index + 1]
            while i < iterations:
                if sort_order[string_left[i]] < sort_order[string_right[i]]:
                    break
                elif sort_order[string_left[i]] == sort_order[string_right[i]]:
                    pass
                else:
                    return 0
                i += 1
            if len(string_left) > len(string_right):
                return 0

        return 1

# alternative approach

class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        sort_order = dict()
        for index, char in enumerate(B):
            sort_order[char] = index

        iterations = len(A) - 1
        for index in range(iterations):
            flag = 0
            string_left = A[index]
            string_right = A[index + 1]
            repetitions = min(len(string_left), len(string_right))
            for index in range(repetitions):
                if sort_order[string_left[index]] != sort_order[string_right[index]]:
                    if sort_order[string_left[index]] > sort_order[string_right[index]]:
                        return 0
                    flag = 1
                    break

            if not flag:
                if len(string_left) > len(string_right):
                    return 0

        return 1