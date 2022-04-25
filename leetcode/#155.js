// question --> https://leetcode.com/problems/min-stack/

// JS ES06 class syntax

class MinStack {
    constructor () {
        this.stack = []; 
        this.minStack = [];
    }
    
    push (val) {
        if (!this.stack.length) {
            this.stack.push(val); 
            this.minStack.push(val); 
        } else {
            this.stack.push(val); 
            this.minStack.push(Math.min(this.minStack[this.minStack.length - 1], val));
        }
    }
    
    pop () {
        if (!this.stack.length) {
             return null; 
        } else {
            this.minStack.pop(); 
            return this.stack.pop(); 
        }
    }
    
    top () {
        return this.stack[this.stack.length - 1]; 
    }
    
    getMin () {
        return this.minStack[this.minStack.length - 1]; 
    }
}

// TC: O(N); SC: O(N)

// end 