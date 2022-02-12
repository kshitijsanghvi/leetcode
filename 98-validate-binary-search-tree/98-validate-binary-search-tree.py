# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        
        def check_sorted(a):
            prev = -math.inf
            for i in a:
                if i > prev:
                    prev = i
                else:
                    return False
            return True
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        return check_sorted(inorder(root))
                
            
            