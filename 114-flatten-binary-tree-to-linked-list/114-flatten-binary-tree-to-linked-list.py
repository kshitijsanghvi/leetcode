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
        
        def po(node):
            if not node:
                return []
            return [node.val] + po(node.left) + po(node.right)
        
        
        
        ans = po(root)
        
        n = len(ans)
        if n == 0:
            return None
        else:
            root.val = ans[0]
            root.left = None
            curr = root
            for i in range(1,n):
                curr.right = TreeNode(ans[i])
                curr = curr.right
            return root