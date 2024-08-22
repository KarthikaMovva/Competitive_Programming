class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0] 
        for char in s:
            if char == '(':
                stack.append(0)  
            else:
                v = stack.pop() 
                stack[-1] += max(2 * v, 1)  
            
        return stack.pop()