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
        if not root:
            return None
        queue = [root]
        while queue:
            new_queue = []
            n = len(queue)
            for i in range(n):
                queue[i].next = queue[i+1] if i + 1 < n else None
                if queue[i].left:
                    new_queue.append(queue[i].left)
                if queue[i].right:
                    new_queue.append(queue[i].right)
            queue = new_queue
        return root