# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -math.inf
        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            
            max_sum = max(max_sum, left + right + node.val, left + node.val, right + node.val, node.val)
            
            return max(left + node.val, right + node.val, node.val)
        
        helper(root)
        return max_sum