# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        cp_head = head
        k = n
        curr = head
        prev = None
        while curr!= None:
            if k > 1:
                k -=1
                
            else:
                if k == 1:
                    lagger = cp_head
                    k-=1

                else:
                    prev = lagger 
                    lagger = lagger.next
            curr = curr.next
            
        if prev == None:
            head = lagger.next
        else:
            prev.next = lagger.next
        
        return head