// question --> https://leetcode.com/problems/reverse-words-in-a-string/

/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let ans = new Array(); 
    let start = 0; 
    let end = 0; 
    let space = ' ';
    s = s.trim() + space; 
    let spaceFlag = false; 
    for (let index = 0; index < s.length; index++) {
        if ((s[index] !== space) && (!spaceFlag)) {
            start = index; 
            spaceFlag = true; 
        } else if (((s[index] === space) && (spaceFlag))) {
            end = index; 
            ans.push(s.slice(start, end));
            spaceFlag = false; 
        } 
    } 
    let i = 0; 
    let j = ans.length - 1; 
    while (i <= j) {
        [ans[i], ans[j]] = [ans[j], ans[i]];
        i += 1; 
        j -= 1;
    }
    return ans.join(' ');
 };
 
 // TC: O(N); SC: O(N)
