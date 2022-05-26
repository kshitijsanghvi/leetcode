# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {v:i for i,v in enumerate(inorder)}
        def helper(preo,ino):
            if not preo:
                return None
            cn = TreeNode(preo[0])
            i = d[cn.val] - d[ino[0]]
            cn.left = helper(preo[1:i+1],ino[:i])
            cn.right = helper(preo[i+1:],ino[i+1:])
            return cn
        
        return helper(preorder,inorder)
        