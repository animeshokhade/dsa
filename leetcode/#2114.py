# question --> https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = float('-inf')
        array_length = len(sentences)
        for string in sentences:
            word_count = len(string.split())
            max_words = max(max_words, word_count)
        return max_words
    '''
    TC: O(N^2)
    SC: O(1)
    '''

    