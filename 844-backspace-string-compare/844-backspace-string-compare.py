class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1 = []
        stack_2 = []
        
        for c in s:
            if c == '#':
                if stack_1:
                    stack_1.pop()
            else:
                stack_1.append(c)
        
        for c in t:
            if c == '#':
                if stack_2:
                    stack_2.pop()
            else:
                stack_2.append(c)
                
                
        if len(stack_1) != len(stack_2):
            return False
        
        else:
            for i, j in zip(stack_1,stack_2):
                if i != j:
                    return False
            return True