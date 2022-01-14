# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        #Form Tree
        # while Postorder != []
        # root = postorder.pop()
        # idx = inorder.index(root)
        # left tree = inorder()
        
        def helper(inorder,postorder):
            if not postorder:
                return None
            
            root = postorder.pop()
            idx = inorder.index(root)
            li = inorder[:idx]
            ri = inorder[idx+1:]
            lp = postorder[:idx]
            rp = postorder[idx:]
            
            node = TreeNode(root)
            node.left = helper(li,lp)
            node.right = helper(ri,rp)
            return node
        
        return helper(inorder,postorder)
            