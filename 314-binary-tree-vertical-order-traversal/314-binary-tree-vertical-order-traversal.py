# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)
        
        q = [[root,0]]
            
        while q:
            cn,cd = q.pop(0)
            if cn:
                d[cd].append(cn.val)
                if cn.left:
                    q.append([cn.left,cd-1])
                if cn.right:
                    q.append([cn.right,cd+1])
                
        return [d[i] for i in sorted(d.keys())]