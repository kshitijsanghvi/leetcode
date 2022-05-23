# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        q = deque()
        q.append(root)
        
        def sysm(q):
            l = 0 
            r = len(q) - 1
            while l < r:
                
                if not q[l] or not q[r]:
                    if q[l] != q[r]:
                        return False
                
                elif q[l] and q[r]:
                    if q[l].val != q[r].val:
                        return False
                
                l += 1
                r -= 1

            return True
        
        while q:
            temp_q = deque()
            
            for i in q:
                temp_q.append(i.left)
                temp_q.append(i.right)
            
            if not sysm(temp_q):
                return False
            
            q = [i for i in temp_q if i != None]
        
        return True
        
        