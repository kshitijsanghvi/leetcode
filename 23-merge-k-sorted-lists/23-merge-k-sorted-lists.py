# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = []
        count = []
        for i,node in enumerate(lists):
            
            if node:
                heapq.heappush(h,[node.val,i,1,node.next])
                
        head = None
        prev = None
        while h:
            cv,listno,nodeno,nn = heapq.heappop(h)
            cn = ListNode(cv)
            if not head:
                head = cn
            if prev:
                prev.next = cn
            prev = cn
            
            if nn:
                heapq.heappush(h,[nn.val,listno,nodeno+1,nn.next])
                
        return head
            
