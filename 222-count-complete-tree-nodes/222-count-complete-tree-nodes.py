# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        1
        |   |
        1   1
        |
        11  11
        
        """
        if not root:
            return 0
        def compute_depth(node):
            if not node:
                return 0
            
            return 1 + compute_depth(node.left)
        
        
        def check(node,idx,d):
            # nodes from 1 - 2**d
            if d == 0:
                if node:
                    return True 
                else:
                    return False
                
            if idx < 2**d//2:
                return check(node.left,idx,d-1)
            else:
                return check(node.right,idx-2**(d-1),d-1)
                
            
        
        d = compute_depth(root) - 1
        
        l = 0
        r = 2**d - 1
        
        """
        [1,1,1,[0,0,0]
        """
        
        while l+1 < r:
            mid = l + (r - l)//2
            if check(root,mid,d):
                l = mid
            else:
                r = mid - 1
        if check(root,r,d):
            return 2 ** (d) - 1 + r + 1
        else:
            return 2 ** (d) - 1 + l + 1
            