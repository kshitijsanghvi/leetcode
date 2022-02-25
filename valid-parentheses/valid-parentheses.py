class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for i  in s:
            if i == ')' or i == '}' or i == ']':
                if i == ')':
                    target = '('
                elif i == '}':
                    target = '{'
                elif i == ']':
                    target = '['
                
                flag = True
                if stack:
                    cv = stack.pop()
                    if cv == target:
                        flag = False
                        
                if flag:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
                        