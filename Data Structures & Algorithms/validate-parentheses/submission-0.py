class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for i in range(len(s)):

            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                element = 0
                if len(stack) != 0:
                    element = stack.pop()
                else:
                    return False
                if s[i] == ')' and element != '(':
                    return False
                elif s[i] == ']' and element != '[':
                    return False
                elif s[i] == '}' and element != '{':
                    return False

        if len(stack) != 0:
            return False

        return True