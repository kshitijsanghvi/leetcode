# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d = {}
        
        def traverse(node):
            if not node:
                return ['NULL']
            
            b = [node.val] + ['|'] +  traverse(node.left) + ['|'] + traverse(node.right)
            a = tuple(b)
            
            if a in d:
                d[a][1]+=1
            else:
                d[a] = [node,1]
                
            return b
        
        traverse(root)
        
       
        return [d[i][0] for i in d if d[i][1]>1]
  
    