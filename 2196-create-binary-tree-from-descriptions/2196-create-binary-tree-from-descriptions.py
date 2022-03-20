# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        child = {}
        
        for p,c,l in descriptions:
            if p not in d:
                d[p] = TreeNode(p)
            if c not in d:
                d[c] = TreeNode(c)
            child[c] = 1    
            if l == 1:
                d[p].left = d[c]
            else:
                d[p].right = d[c]
        
        for i in d:
            if i not in child:
                return d[i]
        return None
        
            