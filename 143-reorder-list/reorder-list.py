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
        
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        second=slow
        slow=slow.next
        second.next=None
        
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        curr=head
        while prev:
            nextp=curr.next
            curr.next=prev
            pnext=prev.next
            prev.next=nextp
            curr=nextp
            prev=pnext
        



        