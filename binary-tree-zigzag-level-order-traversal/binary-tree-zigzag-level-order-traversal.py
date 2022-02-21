# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        q = [root]
        i = 0
        ans = []
        while q:
            temp = [r.val for r in q]
            if i%2 == 0:
                ans.append(temp)
            else:
                ans.append(temp[::-1])
            new_q = []
            for nn in q:
                if nn.left:
                    new_q.append(nn.left)
                if nn.right:
                    new_q.append(nn.right)
            q = new_q
            i+=1
        return ans