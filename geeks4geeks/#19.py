# question --> https://practice.geeksforgeeks.org/problems/kth-smallest-element5635/1/?page=1&status[]=unsolved&sortBy=submissions

class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        if k == 0: return arr[0]
        arr.sort()
        return arr[k - 1]

        # TC: O(NlogN); SC:O(1)

# end 