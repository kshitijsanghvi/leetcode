# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head
        
        odd_head = head
        even_head = head.next
        
        prev_odd = odd_head
        prev_even = even_head
        
        curr = prev_even.next
        even_odd = 0
        while curr != None:
            if even_odd % 2 == 0:
                prev_odd.next = curr
                prev_odd = curr
            else:
                prev_even.next = curr
                prev_even = curr
            curr = curr.next
            even_odd+=1
            
        prev_odd.next = even_head
        prev_even.next = None
        return odd_head