# question --> https://practice.geeksforgeeks.org/problems/wave-array-1587115621/1/?page=1&status[]=unsolved&curated[]=8&sortBy=submissions#

from typing import List


class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        for index in range(0, n - 1, 2):
            a[index], a[index + 1] = a[index + 1], a[index]
        for ele in a:
            print(ele, end = ' ')
        print()

        # TC: O(N); SC: O(1)

# end 