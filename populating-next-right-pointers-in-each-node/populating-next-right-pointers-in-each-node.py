"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        def helper(node,pi,lr):
            if not node:
                return 
            if lr == 0:
                node.next = pi.right
            else:
                if pi.next:
                    node.next = pi.next.left

            helper(node.left,node,0),helper(node.right,node,1)
        
        
        helper(root.left,root,0)
        helper(root.right,root,1)
        return root
            