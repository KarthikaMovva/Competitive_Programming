class Solution(object):
    def calculate(self, s):
        stack = []
        presentnum = 0
        symbol = '+'
        
        for i, char in enumerate(s):
            if char.isdigit():
                presentnum = presentnum * 10 + int(char)
                
            if char in "+-*/" or i == len(s) - 1:
                if symbol == '+':
                    stack.append(presentnum)
                elif symbol == '-':
                    stack.append(-presentnum)
                elif symbol == '*':
                    stack.append(stack.pop() * presentnum)
                elif symbol == '/':
                    lastdigit = stack.pop()
                    if lastdigit < 0:
                        stack.append(-(-lastdigit // presentnum))
                    else:
                        stack.append(lastdigit // presentnum)
                
                symbol = char
                presentnum = 0
        
        return sum(stack)
        