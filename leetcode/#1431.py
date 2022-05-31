# question --> https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        size = len(candies)
        result = [True] * size
        for index in range(size):
            if candies[index] + extraCandies < max_candy:
                result[index] = False
        return result

    '''
    TC: O(N)
    SC: O(N)
    '''
