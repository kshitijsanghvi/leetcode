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
        def helper(node,d):
            nonlocal ans
            if not node:
                return 
            
            if node.val in d:
                d[node.val]+=1
            else:
                d[node.val] = 1

            if node.left:
                helper(node.left, dict(d))
            if node.right:
                helper(node.right, dict(d))
            
            if node.left == node.right == None:        
                count_off = sum([1 for i in d if d[i]%2 == 1])
                ans += 1 if count_off <= 1 else 0

            
            
        helper(root,dict())
        return ans