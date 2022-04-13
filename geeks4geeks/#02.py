# question --> https://practice.geeksforgeeks.org/problems/reverse-a-string/1/?page=1&difficulty[]=-1&category[]=Strings&sortBy=submissions#

def reverseWord(s):
    #your code here
    string = list(s)
    start, end = 0, len(s) - 1
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1
    return ''.join(string)

    # TC: O(|S|); SC: O(1) 
