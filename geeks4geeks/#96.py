# question --> https://practice.geeksforgeeks.org/problems/vowel-or-not0831/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

class Solution:
    def isVowel(ob, c):
        # code here
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        if c in vowels:
            return 'YES'
        return 'NO'

    # TC: O(1); SC: O(1)
