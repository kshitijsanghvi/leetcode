# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def traverse(node,t,p):
            if node.val == t:
                return True
            
            if node.left and traverse(node.left,t,p):
                p.append('L')
                return True
            
            elif node.right and traverse(node.right,t,p):
                p.append('R')
                return True
            
            return False
        
        p = []
        traverse(root,startValue,p)
        s = p[::-1]
        p = []
        traverse(root,destValue,p)
        d = p[::-1]
        
        
        i = 0
        while i < len(s) and i < len(d) and s[i] == d[i]:
            i+=1 
        
        return 'U'*(len(s)-i) + ''.join(d[i:])
        