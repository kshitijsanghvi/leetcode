# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        
        if p.right:
            ans = p.right
            p = p.right
            while p.left:
                ans = p.left
                p = p.left
            return ans
        else:
            temp = root
            stack = []
            while temp.val != p.val:
                if temp.val > p.val:
                    stack.append(["left",temp])
                    temp = temp.left
                else:
                    stack.append(['right',temp])
                    temp = temp.right
            if not stack:
                return None
            while stack and stack[-1][0]!='left':
                stack.pop()
            if stack:
                return stack[-1][1]
            else:
                return None
            