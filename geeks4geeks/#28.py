# question --> https://practice.geeksforgeeks.org/problems/palindromic-array-1587115620/1/?page=1&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

def PalinArray(arr ,n):
    # Code here
    for index in range(n):
        temp = str(arr[index])
        start = 0
        end = len(temp) - 1
        while start <= end:
            if temp[start] != temp[end]: return 0
            start += 1
            end -= 1
    return 1

    # TC: O(N^2); SC: O(1)
# end 