# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        q = deque()
        q.append(root)
        ans = []
        ans.append(root.val)
        
        while q:
            temp_q = deque()
            for i in q:
                if i.left:
                    temp_q.append(i.left)
                if i.right:
                    temp_q.append(i.right)
            
            if temp_q:
                ans.append(temp_q[-1].val)
            
            q = temp_q
            
        return ans
            
                