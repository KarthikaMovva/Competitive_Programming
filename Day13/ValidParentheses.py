class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}
        for each in s:
            if each in pairs:
                topElement = stack.pop() if stack else '#'
                if pairs[each] != topElement:
                    return False
            else:
                stack.append(each)
        return not stack
        