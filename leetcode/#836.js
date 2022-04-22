// question --> https://leetcode.com/problems/rectangle-overlap/

/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
var isRectangleOverlap = function(rec1, rec2) {
    if (rec1[3] <= rec2[1] || rec1[1] >= rec2[3] || rec1[2] <= rec2[0] || rec1[0] >= rec2[2]) {
        return 0
    }
    return 1
};
        
// TC: O(1); SC: O(1)

// end 