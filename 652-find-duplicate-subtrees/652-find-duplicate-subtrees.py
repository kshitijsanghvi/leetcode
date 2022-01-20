# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d = {}
        ans = {}
        
        def traverse(node):
            if not node:
                return ["NULL"]
            
            a = tuple([node.val] + ['|'] +  traverse(node.left) + ['|'] + traverse(node.right))
            if a in d:
                if d[a] not in ans:
                    ans[d[a]] = 1
            else:
                d[a] = node
                
            return list(a)
        
        traverse(root)
        return ans.keys()
    