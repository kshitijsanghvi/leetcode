# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = None
        def helper(node1, node2):
            nonlocal ans
            if not node1:
                return 
            
            if node1 == target:
                ans = node2
            else:
                helper(node1.left,node2.left)
                helper(node1.right, node2.right)
        helper(original,cloned)
        return ans