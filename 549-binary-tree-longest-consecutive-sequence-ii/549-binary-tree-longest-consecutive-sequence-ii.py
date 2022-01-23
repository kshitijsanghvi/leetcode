# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_l = float('-inf')
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            if not node:
                return [0,0]
            
            cans = [1,1]
            lnr = 1
            
            l = helper(node.left)
            r = helper(node.right)
            
            if node.left and node.left.val == node.val - 1:
                cans[0] = l[0] + 1
            elif node.left and node.left.val == node.val + 1:
                cans[1] = l[1] + 1
                
            if node.right and node.right.val == node.val - 1:
                cans[0] = max(cans[0],r[0] + 1)
            elif node.right and node.right.val == node.val + 1:
                cans[1] = max(cans[1],r[1] + 1)
                
            if node.left and node.right and node.left.val + 1 == node.val == node.right.val - 1:
                lnr = max(lnr,l[0]+r[1]+1)
            if node.left and node.right and node.left.val - 1 == node.val == node.right.val + 1:
                lnr = max(lnr,l[1]+r[0]+1)
                
            self.max_l = max(self.max_l,lnr,max(l),max(r))
            return cans
            
        return max(helper(root)+[self.max_l])    
                