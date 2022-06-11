# question --> https://practice.geeksforgeeks.org/problems/remove-vowels-from-string1446/1/?page=2&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def removeVowels(self, S):
        # code here
        S = list(S)
        for index, char in enumerate(S):
            if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
                S[index] = ''
        return ''.join(S)

    # TC: O(|s|); SC: O(1)
