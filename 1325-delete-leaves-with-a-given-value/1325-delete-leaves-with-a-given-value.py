# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        
        def helper(node):
            if node.left == None and node.right == None:
                if node.val == target:
                    return True
                return False
            
            if node.left:
                l = helper(node.left)
                if l:
                    node.left = None
            if node.right:
                r = helper(node.right)
                if r:
                    node.right = None
            
            if node.val == target and node.left == None and node.right == node.left:
                return True
            return False
        
        return root if helper(root) == False else None