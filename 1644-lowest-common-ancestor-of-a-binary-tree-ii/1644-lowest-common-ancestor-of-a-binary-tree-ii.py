# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        start = {}
        end = {}
        counter = 0
        found_p = 0
        found_q = 0
        lca = None
        def dfs(node):
            nonlocal start,end,counter,found_p,found_q,lca
            
            if not node:
                return 
            
            start[node] = counter
            counter += 1
            
            dfs(node.left)
            dfs(node.right)
            
            end[node] = counter
            counter += 1
            
            if node == p:
                found_p = True
            if node == q:
                found_q = True
                
            if found_q and found_p:
                if start[node] <= min(start[p],start[q]) and end[node] >= max(end[p],end[q]):
                    if not lca:
                        lca = node
        dfs(root)
        return lca