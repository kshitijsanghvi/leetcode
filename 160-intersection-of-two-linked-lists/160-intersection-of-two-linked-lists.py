# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        temp1 = headA
        n1 = 0
        while temp1:
            temp1 = temp1.next
            n1+=1
        temp2 = headB
        n2 = 0
        while temp2:
            temp2 = temp2.next
            n2+=1
        
        if n2 < n1:
            headA,headB = headB,headA
        
        p1 = headA
        p2 = headB
        
        d = abs(n2-n1)
        while d:
            p2 = p2.next
            d-=1
        
        while p1 and p2 and p1 != p2:
            p1 = p1.next
            p2 = p2.next
            
        return p1 if p1 else None
