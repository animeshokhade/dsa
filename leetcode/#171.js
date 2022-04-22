// question --> https://leetcode.com/problems/excel-sheet-column-number/

/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    let index = new Array(); 
    index = ['A',
             'B',
             'C',
             'D',
             'E',
             'F',
             'G',
             'H',
             'I',
             'J',
             'K',
             'L',
             'M',
             'N',
             'O',
             'P',
             'Q',
             'R',
             'S',
             'T',
             'U',
             'V',
             'W',
             'X',
             'Y',
             'Z'];
    
    let summ = 0; 
    let i = 0; 
    
    for (let j = 0; j < columnTitle.length; j++) {
        for (let stringIndex = 0; stringIndex < index.length; stringIndex++) {
            if (columnTitle[j] == index[stringIndex]) {
            let position = stringIndex;
            let weight = position + 1; 
            summ += weight * (Math.pow(26, (columnTitle.length - 1 - i)));
            i += 1;
        }
        }
    }
    return summ; 
};

// TC: O(N^2); SC: O(1) 

// Optimised Approach

/**
 * @param {string} columnTitle
 * @return {number}
 */
var titleToNumber = function(columnTitle) {
    let summ = 0; 
    let base = 'A';
    for (let index = 0; index < columnTitle.length; index++) {
        let weight = columnTitle.charCodeAt(index) - base.charCodeAt(0) + 1;
        summ += weight * Math.pow(26, (columnTitle.length - 1 - index));
    }
    return summ;
};

// TC: O(N); SC: O(1)

// end