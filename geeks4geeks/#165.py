# question --> https://practice.geeksforgeeks.org/problems/minimum-distance-between-two-numbers/1/?page=1&difficulty[]=-1&status[]=unsolved&sortBy=submissions#

class Solution:
    def minDist(self, arr, n, x, y):
        if x not in arr or y not in arr:
            return -1

        dis = float('inf')
        pre_x = -1
        pre_y = -1

        p = 0

        while p < n:
            if arr[p] == x:
                if pre_y != -1:
                    dis = min(dis, abs(p - pre_y))
                pre_x = p
            elif arr[p] == y:
                if pre_x != -1:
                    dis = min(dis, abs(p - pre_x))
                pre_y = p
            p += 1

        return dis

        # TC: O(N); SC: O(1)
