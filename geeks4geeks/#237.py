# question --> https://practice.geeksforgeeks.org/problems/longest-substring-containing-1/1/?page=1&difficulty[]=-1&status[]=unsolved&category[]=Strings&sortBy=submissions#

def maxlength(s):
    # add code here
    cnt = 0
    one = 0
    for ch in s:
        if ch == '1':
            cnt += 1
        else:
            one = max(cnt, one)
            cnt = 0
    one = max(cnt, one)
    return one

    # TC: O(N); SC: O(1) 