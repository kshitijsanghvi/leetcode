# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_v = -math.inf
        def helper(node):
            nonlocal max_v
            if not node:
                return 0
            
            else:
                left = helper(node.left)
                right = helper(node.right)
                
                max_v = max(max_v, left + right + 1)
                
                return 1 + max(left, right)
        helper(root)
        return max_v - 1