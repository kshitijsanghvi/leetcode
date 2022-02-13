# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        
        ans = None
        
        def helper(node,k):
            nonlocal ans
            if not ans:
                if not node:
                    return 0

                left = helper(node.left,k)
                if left == k - 1:
                    ans = node.val
                right = helper(node.right,k - left - 1)
                return left + 1 + right
            return math.inf
        helper(root,k)
        return ans