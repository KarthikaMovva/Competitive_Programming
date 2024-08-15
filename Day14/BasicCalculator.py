class Solution(object):
    def calculate(self,s):
        stack = []
        presentnumber = 0
        ans = 0
        operator = 1
        for char in s:
            if char.isdigit():
                presentnumber = presentnumber * 10 + int(char)
            elif char == '+':
                ans += operator * presentnumber
                operator = 1
                presentnumber = 0
            elif char == '-':
                ans += operator * presentnumber
                operator = -1
                presentnumber = 0
            elif char == '(':
                stack.append(ans)
                stack.append(operator)
                operator = 1
                ans = 0
            elif char == ')':
                ans += operator * presentnumber
                ans *= stack.pop()
                ans += stack.pop()
                presentnumber = 0

        return ans + operator * presentnumber