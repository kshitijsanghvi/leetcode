# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            ans.append([r.val for r in q])
            new_q = []
            for n in q:
                if n.left:
                    new_q.append(n.left)
                if n.right:
                    new_q.append(n.right)
            q = new_q
        return ans