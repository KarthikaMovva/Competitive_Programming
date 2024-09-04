class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        correspond_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtrack(index, path):
            if index == len(digits):
                possiblecombinations.append("".join(path))
                return
            possiblestring = correspond_char[digits[index]]
            for character in possiblestring:
                path.append(character) 
                backtrack(index + 1, path)  
                path.pop() 
    
        possiblecombinations = []
        backtrack(0, [])
        return possiblecombinations
        
        