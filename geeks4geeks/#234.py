# question --> https://practice.geeksforgeeks.org/problems/reverse-a-string-using-stack/1/?page=7&status[]=unsolved&sortBy=submissions#

def reverse(S):
    # Add code here
    stack = []
    for ch in S:
        stack.append(ch)

    ret = []
    while stack:
        ret.append(stack.pop())

    return ''.join(ret)

    # TC: O(N); SC: O(N)