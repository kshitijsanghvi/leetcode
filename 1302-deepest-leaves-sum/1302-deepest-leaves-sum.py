# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """
        Create a dictionary and sum all elements at equal depth
        find max key and return 
        """
        
        if not root:
            return None
        
        else:
            
            d = Counter()
            
            def helper(node,depth):
                if node:
                    if not node.left and not node.right:
                        d[depth] += node.val
                    else:
                        helper(node.left,depth+1)
                        helper(node.right,depth + 1)
            # I forget to call the helper function before returning
            
            helper(root,0)
            return d[max(d.keys())]
                    