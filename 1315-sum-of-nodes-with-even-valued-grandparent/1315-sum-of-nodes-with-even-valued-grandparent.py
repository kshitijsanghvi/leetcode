# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0
        
        def helper(node):
            nonlocal ans
            if not node:
                return
            
            if node.val %2 == 0:
                if node.left and node.left.left:
                    ans+= node.left.left.val
                if node.left and node.left.right:
                    ans+=node.left.right.val
                if node.right and node.right.left:
                    ans+= node.right.left.val
                if node.right and node.right.right:
                    ans+=node.right.right.val
                    
            helper(node.left)
            helper(node.right)
            
        helper(root)
        return ans