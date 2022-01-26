# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        
        def traverse(node):
            nonlocal ans
            if not node:
                return []
            
            return traverse(node.left) + [node.val] + traverse(node.right)
        
        ans = traverse(root)
        
        l = 0
        r = len(ans) - 1
        
        while l < r:
            s = ans[l] + ans[r] 
            if s == k:
                return True
            elif s > k:
                r -=1
            else:
                l+=1
                
        return False