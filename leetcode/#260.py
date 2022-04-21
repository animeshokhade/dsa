# question --> https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        lookup = set()

        for number in nums: 
            if number in lookup: 
                lookup.remove(number)
            elif number not in lookup: 
                lookup.add(number)

        return sorted(lookup) 
        
        # TC: O(NlogN); SC: O(N)
        
# end

# Editorial (Bit Manipulation) 

