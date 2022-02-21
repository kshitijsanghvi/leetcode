# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        if p.right:
            ans = p.right
            p = p.right
            while p.left:
                ans = p.left
                p = p.left
            return ans
        else:
            temp = root
            prev = None
            while temp.val != p.val:
                if temp.val > p.val:
                    prev = temp
                    temp = temp.left
                else:
                    temp = temp.right
            if not prev:
                return None
            return prev