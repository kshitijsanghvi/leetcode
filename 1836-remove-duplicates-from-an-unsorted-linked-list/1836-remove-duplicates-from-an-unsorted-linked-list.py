# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        curr = head
        d = Counter()
        while curr:
            d[curr.val]+=1
            curr = curr.next
        nhead = None
        prev = None
        
        curr = head
        while curr:
            if d[curr.val] == 1:
                if prev:
                    prev.next = curr
                    prev = curr
                else:
                    nhead = curr
                    prev = curr
            curr = curr.next
        
        if prev:
            prev.next = None
        return nhead
                    