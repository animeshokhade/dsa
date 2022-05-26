# question --> https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1/?page=1&status[]=unsolved&sortBy=submissions#

class Solution:
    def sort012(self,arr,n):
        # code here
        start, mid = 0, 0
        end = n - 1
        while mid <= end:
            if arr[mid] == 1:
                mid += 1
            elif arr[mid] == 0:
                arr[start], arr[mid] = arr[mid], arr[start]
                start += 1
                mid += 1
            elif arr[mid] == 2:
                arr[mid], arr[end] = arr[end], arr[mid]
                end -= 1
        return arr

        # TC:O(N); SC:O(1)
# end 