# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @lru_cache(None)
        def helper(i,j):
            if j < i:
                return [None]
            if i == j:
                return [TreeNode(i)]
    
            cans = []
            for k in range(i,j+1):
                left = helper(i,k-1)
                right = helper(k+1,j)
                
                for l in left:
                    for r in right:
                        cn = TreeNode(k)
                        cn.left = l
                        cn.right = r
                        cans.append(cn)
            return cans
        return helper(1,n)        