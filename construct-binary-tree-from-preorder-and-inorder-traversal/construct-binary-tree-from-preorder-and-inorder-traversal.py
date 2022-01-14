# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder,inorder):
            if not inorder:
                return None
            
            root = preorder.pop(0)
            idx = inorder.index(root)
            li = inorder[:idx]
            ri = inorder[idx+1:]
            lp = preorder[:idx]
            rp = preorder[idx:]
            node = TreeNode(root)
            node.left = helper(lp,li)
            node.right = helper(rp,ri)
            
            return node
        return helper(preorder,inorder)
            