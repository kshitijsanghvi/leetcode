# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not l1:
            return l2
        if not l2:
            return l1
        
        
        s1 = l1
        s2 = l2
        
        c = 0
        p_s1 = None
        
        while s1 != None and s2 != None:
            s1.val = s2.val + s1.val + c
            c = s1.val//10
            s1.val = s1.val % 10
            p_s1 = s1
            s1 = s1.next
            s2= s2.next
            
        while s1 != None:
            s1.val = s1.val + c
            c = s1.val//10
            s1.val = s1.val % 10
            p_s1 = s1
            s1 = s1.next
            
        while s2 != None:
            cn = ListNode()
            s2.val = s2.val + c
            c = s2.val//10
            s2.val = s2.val % 10
            cn.val = s2.val
            p_s1.next = cn
            p_s1 = cn
            s2 = s2.next
        
        if c == 1:
            cn = ListNode(1)
            p_s1.next = cn
            
        return l1
            