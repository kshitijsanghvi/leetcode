"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        if head.val == insertVal:
            cn = Node(insertVal)
            cn.next = head.next
            head.next = cn
            return head
        
        cn = head
        prev = None
        while cn.next.val >= cn.val and cn.next != head:
            prev = cn
            cn = cn.next
            
        prev = cn
        if cn.next == head:
            
            root = head
        else:
            root = cn.next

        
        cn = root
        
        while cn.next!= root and cn.val < insertVal:
            prev = cn
            cn = cn.next
            
        if cn.next == root and cn.val < insertVal:
            cn.next = Node(insertVal)
            cn.next.next = root
            return head
        else:
            nn = Node(insertVal)
            nn.next = cn
            prev.next = nn
            return head