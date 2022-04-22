# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        d = {}
        def helper(node):
            if not node:
                return 
            else:
                helper(node.left)
                d[node.val] = node       
                ans.append(node.val)
                helper(node.right)
                
        helper(root)
        # print(ans)
        i1 = None
        i2 = None
        for i in range(1,len(ans)):
            if ans[i] < ans[i-1]:
                i1 = i - 1
                break
        for i in range(len(ans)-1,0,-1):
            if ans[i-1] > ans[i]:
                i2 = i
                break
        d[ans[i1]].val = ans[i2]
        d[ans[i2]].val = ans[i1]
        return root