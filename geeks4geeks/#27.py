# question --> https://practice.geeksforgeeks.org/problems/check-for-binary/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

def isBinary(str):
    # code here
    for char in str:
        if char != '0' and char != '1': return 0
    return 1

    # TC: O(|s|); SC: O(1)
# end
