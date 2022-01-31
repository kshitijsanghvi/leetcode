# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        
        def helper(n):
            if n == 1:
                return [TreeNode(0)]
            
            ree = n - 1
            s = 0
            ans = []
            for i in range(1,ree,2):
                
                l = helper(i) 
                r = helper(ree - i)
                for nnl in l:
                    for nnr in r:
                        rr = TreeNode(0)
                        rr.left = nnl
                        rr.right = nnr
                        ans.append(rr)
            return ans
            
        return helper(n)