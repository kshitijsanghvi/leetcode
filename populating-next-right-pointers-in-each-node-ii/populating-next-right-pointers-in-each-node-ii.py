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
    def connect(self, root: 'Node') -> 'Node':
        di = defaultdict(list)
        def explore(node,d):
            if not node:
                return
            if len(di[d]) != 0:
                di[d][-1].next = node
            di[d].append(node)
            if node.left:
                explore(node.left,d+1)
            if node.right:
                explore(node.right,d+1)
            return
        
        explore(root,0)
        return root
            
                    
            