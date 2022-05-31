# question --> https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0  # minimum wealth possible
        n = len(accounts)
        for index in range(n):
            max_wealth = max(max_wealth, sum(accounts[index]))
        return max_wealth

    '''
    TC: O(M * N)
    SC: O(1)
    '''
