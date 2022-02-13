# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        
        def add(node,depth):
            if not node:
                return 
            d[depth].append(node.val)
            add(node.left,depth+1)
            add(node.right,depth+1)
        add(root,0)  
        return [d[i] for i in d]