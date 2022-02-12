# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_v = -math.inf
        
        def helper(root):
            nonlocal max_v
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            max_v = max(max_v,root.val,root.val + left,root.val + right, root.val + left + right)
            
            return max(root.val, root.val + left, root.val + right)
        
        helper(root)
        
        return max_v