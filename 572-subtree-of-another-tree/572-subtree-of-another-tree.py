# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root1,root2,s=0):
            if not root1 or not root2:
                if root1 == root2:
                    return True
                else:
                    return False
            op1 = False
            if root1.val == root2.val:
                op1 = helper(root1.left,root2.left,1) and helper(root1.right,root2.right,1)
            if s == 1 or op1:
                return op1
            else:
                return helper(root1.left,root2) or helper(root1.right,root2)
        return helper(root,subRoot)
            