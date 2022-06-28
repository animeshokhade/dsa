# question --> https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        rom = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        ret = ''

        while num:
            div = 0

            for r in rom:
                if num // r != 0:
                    div = max(div, r)

            mul = num // div
            ret += mul * rom[div]
            num %= div

        return ret

    # TC: O(1); SC: O(1)

# clean

from collections import OrderedDict


class Solution:
    def intToRoman(self, num: int) -> str:
        rom = OrderedDict({
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        })

        ret = ''

        for div, sym in rom.items():
            if not num: break
            mul, num = divmod(num, div)
            ret += mul * sym

        return ret

        # TC: O(1); SC: O(1)