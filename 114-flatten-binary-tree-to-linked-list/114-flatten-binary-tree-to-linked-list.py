# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def flatten(node):
            if not node:
                return None
            
            temp = node
            right_tree = node.right
            node.right = flatten(node.left)
            node.left = None
            while node.right!= None:
                node = node.right
            
            node.right = flatten(right_tree)
            return temp
        
        return flatten(root)