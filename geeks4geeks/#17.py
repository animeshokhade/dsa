# question --> https://practice.geeksforgeeks.org/problems/find-transition-point-1587115620/1/?page=1&difficulty[]=-2&difficulty[]=-1&difficulty[]=0&status[]=unsolved&sortBy=submissions#

def transitionPoint(arr, n):
    #Code here
    if 1 in arr:
        return arr.index(1)
    return -1

    # TC:O(N); SC: O(1)

# end 