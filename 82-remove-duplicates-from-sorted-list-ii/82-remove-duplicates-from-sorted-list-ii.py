# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None
        curr = head
        head2 = None
        while curr:
            
            if curr.next and curr.val == curr.next.val:
                val = curr.val
                
                while curr and curr.val == val:
                    curr = curr.next
            else:
                if prev:
                    prev.next = curr
                    prev = curr
                else:
                    prev = curr
                    head2 = prev
                curr = curr.next
                
        if prev:
            prev.next = None
        return head2