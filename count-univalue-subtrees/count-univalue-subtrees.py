# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def helper(node,val):
            if node == None:
                return True
            l = helper(node.left,node.val)
            r = helper(node.right,node.val)
            
            if l and r:
                self.ans+=1
                if node.val == val:
                    return True
            
            return False
        if root:
            helper(root,root.val)
        else:
            return 0
        return self.ans