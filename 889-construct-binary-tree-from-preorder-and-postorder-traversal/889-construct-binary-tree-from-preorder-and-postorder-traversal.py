# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def helper(pre,post):
            if not pre:
                return None
            
            if len(pre) == 1:
                return TreeNode(pre[0])
            
            curr = TreeNode(pre[0])
            idx = post.index(pre[1])
            curr.left = helper(pre[1:2+idx],post[:idx+1])
            curr.right = helper(pre[2+idx:],post[idx+1:-1])
            
            return curr
        
        return helper(preorder,postorder)