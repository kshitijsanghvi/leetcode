# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head.next == None:
            return False
        fast_pointer = slow_pointer = head 
        
        flag = True
        while fast_pointer.next and fast_pointer.next.next and (flag or slow_pointer != fast_pointer):
            flag = False
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            
        if fast_pointer.next and fast_pointer.next.next:
            return True
        else:
            return False