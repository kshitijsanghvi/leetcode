# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        ans = None
        
        def find_height(node):
            nonlocal ans
            if not node:
                return 0
            
            left = find_height(node.left)
            right = find_height(node.right)
            
            if max(left,right) - min(left,right) > 1:
                if ans == None:
                    ans = False
            
            return 1 + max(left,right)
        
        find_height(root)
        return ans if ans != None else True