# question --> https://practice.geeksforgeeks.org/problems/remove-characters-from-alphanumeric-string0648/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

class Solution:
    def removeCharacters(self, S):
        # code here
        digit = ''
        for char in S:
            if char.isdigit():
                digit += char
        return digit

    # TC: O(|S|); SC: O(|S|)


class Solution:
    def removeCharacters(self, S):
        # code here
        S = list(S)
        for index, char in enumerate(S):
            if not char.isdigit():
                S[index] = ''
        return ''.join(S)

    # TC: O(|S|); SC: O(1)
