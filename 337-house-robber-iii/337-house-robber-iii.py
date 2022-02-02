# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        dp = {}
        def helper(node,canRob):
            if not node:
                return 0
            
            if (node,canRob) not in dp:
                if canRob:
                    #deost nob
                    a = helper(node.left,True) + helper(node.right,True)
                    b = node.val + helper(node.left,False) + helper(node.right,False)
                    dp[node,canRob] = max(a,b)
                    
                else:
                    dp[node,canRob] = helper(node.left,True) + helper(node.right,True)
                    
            
            return dp[node,canRob]
        
        return helper(root,True)