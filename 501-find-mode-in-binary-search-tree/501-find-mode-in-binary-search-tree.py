# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int)
        max_count = -math.inf
        
        def helper(root):
            nonlocal max_count,d
            if not root:
                return 
            d[root.val] += 1
            max_count = max(max_count,d[root.val])
            helper(root.left)
            helper(root.right)
            return 
        
        helper(root)
        ans = []
        for i in d:
            if d[i] == max_count:
                ans.append(i)
        return ans
            