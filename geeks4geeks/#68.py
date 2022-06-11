# question --> https://practice.geeksforgeeks.org/problems/upper-case-conversion5419/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions

class Solution:
    def transform(self, s):
        # code here
        s.strip
        s = list(s)
        space = ' '
        convert = True
        for index, char in enumerate(s):
            if convert:
                s[index] = char.upper()
                convert = False
            if char == space:
                convert = True
        return ''.join(s)
        # TC: O(N); SC: O(1)

# clean

class Solution:
    def transform(self, s):
        # code here
        s = s.strip().split()
        s = [char.capitalize() for char in s]
        return ' '.join(s)
        # TC: O(N); SC: O(1)