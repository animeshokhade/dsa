# question --> https://practice.geeksforgeeks.org/problems/time-to-words3728/1/?page=3&difficulty[]=-2&status[]=unsolved&sortBy=submissions#

class Solution:
    def timeToWord(self, H, M):
        # code here
        words = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            21: 'twenty one',
            22: 'twenty two',
            23: 'twenty three',
            24: 'twenty four',
            25: 'twenty five',
            26: 'twenty six',
            27: 'twenty seven',
            28: 'twenty eight',
            29: 'twenty nine'
        }
        if M == 0:
            s = "{} o' clock".format(words[H if H <= 12 else H - 12])
        elif M == 15:
            s = "quarter past {}".format(words[H if H <= 12 else H - 12])
        elif M == 30:
            s = "half past {}".format(words[H if H <= 12 else H - 12])
        elif 0 < M < 30:
            if M == 1:
                s = "one minute past {}".format(words[H if H <= 12 else H - 12])
            else:
                s = "{} minutes past {}".format(words[M], words[H if H <= 12 else H - 12])
        elif M == 45:
            s = "quarter to {}".format(words[H + 1 if H < 12 else (H + 1) - 12])
        else:
            if M == 59:
                s = "{} minute to {}".format(words[60 - M], words[H + 1 if H < 12 else (H + 1) - 12])
            else:
                s = "{} minutes to {}".format(words[60 - M], words[H + 1 if H < 12 else (H + 1) - 12])
        return s

    # TC: O(1); SC: O(1)