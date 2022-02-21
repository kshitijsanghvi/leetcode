# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        def search(node,k):
            nonlocal ans
            if not node:
                return 0
            left_count = search(node.left,k)
            if left_count + 1 == k:
                ans = node.val
                return math.inf
            else:
                right_count = search(node.right,k - left_count - 1)
                
            return left_count + right_count + 1
        
        search(root,k)
        return ans
                