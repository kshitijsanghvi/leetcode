# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = {}
        def helper(node,idx,current_depth):
            nonlocal d
            if not node:
                return
            l = 2 *idx + 1
            r = 2 *idx + 2
            next_depth = current_depth + 1
            if current_depth not in d:
                d[current_depth] = [idx,idx,1]
            else:
                d[current_depth][0] = min(d[current_depth][0],idx)
                d[current_depth][1] = max(d[current_depth][1],idx)
                d[current_depth][2] = d[current_depth][1] - d[current_depth][0] + 1
            
            if node.left:
                helper(node.left,l,next_depth)
            if node.right:
                helper(node.right,r,next_depth)
            
            return 
        helper(root,0,0)
        return max([d[i][2] for i in d])
                
            
            