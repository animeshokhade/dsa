// question --> https://leetcode.com/problems/reverse-string/

/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let start = 0; 
    let end = s.length - 1; 
    while (start <= end) {
        [s[start], s[end]] = [s[end], s[start]];
        start += 1; 
        end -= 1;
    }
    return s;
};

// TC: O(N); SC: O(1)

// end 