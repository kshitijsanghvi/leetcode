# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lhead = None
        lprev = None
        gehead = None
        geprev = None
        
        curr = head
        while curr:
            if curr.val < x:
                if lprev:
                    lprev.next = curr
                    lprev = curr
                else:
                    lhead = lprev = curr
            else:
                if geprev:
                    geprev.next = curr
                    geprev = curr
                else:
                    gehead = geprev = curr
            curr = curr.next
                    
        if lprev:
            lprev.next = gehead
        if geprev:
            geprev.next = None
            
        return lhead if lhead else gehead