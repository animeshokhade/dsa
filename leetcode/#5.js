// question --> https://leetcode.com/problems/longest-palindromic-substring/submissions/

/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let n = s.length; 
    let pal = '';
    for (let i = 0; i < n; i++) {
        // checking for odd length palindromes
        let l = i - 1; 
        let r = i + 1; 
        while ((l >= 0) && (r < n) && (s[l] == s[r])) {
            l -= 1; 
            r += 1; 
        }
        if ((r - l - 1) > pal.length) {
            pal = s.slice(l + 1, r); 
        } else if ((r - l - 1) == pal.length) {
            if (s.indexOf(pal[0]) > 1) {
                pal = s.slice(l + 1, r); 
            }
        }
    }
    for (let i = 0; i < n; i++) {
        // checking for even length palindromes 
        let l = i - 1; 
        let r = i; 
        while ((l >= 0) && (r < n) && (s[l] == s[r])) {
            l -= 1; 
            r += 1;
        }
        if ((r - l - 1) > pal.length) {
            pal = s.slice(l + 1, r); 
        } else if ((r - l - 1) == pal.length) {
            if (s.indexOf(pal[0]) > l) {
                pal = s.slice(l + 1, r); 
            }
        }
    }
    return pal; 
};

// TC: O(N^2); SC: O(N)

// end 