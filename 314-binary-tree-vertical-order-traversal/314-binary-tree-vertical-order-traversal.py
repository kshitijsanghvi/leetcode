# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = defaultdict(list)
        min_v = math.inf
        max_v = -math.inf
        q = [[root,0]]
            
        while q:
            cn,cd = q.pop(0)
            if cn:
                min_v = min(min_v,cd)
                max_v = max(max_v,cd)
                d[cd].append(cn.val)
                if cn.left:
                    q.append([cn.left,cd-1])
                if cn.right:
                    q.append([cn.right,cd+1])
                
        return [d[i] for i in range(min_v,max_v+1) if i in d]