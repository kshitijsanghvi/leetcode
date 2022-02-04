# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        
        copy = head
        i = 0
        
        while head != None:
            q.append(head)
            head = head.next
            
        i = 0
        copy = curr = TreeNode()
        while q:
            if i %2 == 0:
                curr.next = q.popleft()
            else:
                curr.next = q.pop()
            curr = curr.next
            i+=1
            
        curr.next = None
        return copy.next