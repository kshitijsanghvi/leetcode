# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """
        Palindromic Permutations :
        "a" -> d = {a:1}
        "aa" -> d = {a:2}
        
        condition_1 = len(d) == 1 Always a palindrome 
        aabbcc - abccba
        if max(d.keys()) == min(d.keys()) then it is always a palindrome
        if count of all keys is even or except1 then it is always a palindrome
        
        
        To fomalize:
        Main condition if len(d) == 1 -> palindrome
        if count is odd for at most one key it is a palindrome 
        
        """
        ans = 0
        def helper(node,val):
            nonlocal ans
            if not node:
                return 
            
            d = 1 << node.val
            val = val ^ d
            
            if node.left:
                helper(node.left, val)
            if node.right:
                helper(node.right, val)
            if node.left == node.right == None:
                # Check if all 0
                if val == 0 or val & (val - 1) == 0:
                    ans +=1
            
            
        helper(root,0)
        return ans