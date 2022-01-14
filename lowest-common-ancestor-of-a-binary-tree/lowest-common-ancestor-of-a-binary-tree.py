# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.n = None
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node,t):
            if not node:
                return False
            if node == t:
                return True
            return helper(node.left,t) or helper(node.right,t)
        
        if helper(p,q):
            return p
        elif helper(q,p):
            return q
        
        def helper2(node,p,q):
            if not node:
                return False
            
            if node == p or node == q:
                return True
        
            a = helper2(node.left,p,q)
            b = helper2(node.right,p,q)
            
            if a and b:
                self.n = node
                return False
            else:
                return a or b
        helper2(root,p,q)
        return self.n
            