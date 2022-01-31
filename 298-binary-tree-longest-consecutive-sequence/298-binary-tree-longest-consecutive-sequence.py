# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        max_l = float('-inf')
        
        
        def helper(root):
            nonlocal max_l
            if not root:
                return 0 
            
            l = helper(root.left)
            r = helper(root.right)
            lc = 1
            rc = 1
            
            if root.left and root.left.val == root.val + 1:
                lc = l + 1
            if root.right and root.right.val == root.val + 1:
                rc = r + 1
            
            cmax = max(lc,rc)
            max_l = max(max_l,cmax)
            
            return cmax
        
        helper(root)
        return max_l