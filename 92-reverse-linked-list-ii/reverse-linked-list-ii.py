# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(-501,head)
        lp=dummy
        for i in range(left-1):
            lp=lp.next
        curr=lp.next
        prev=None
        for i in range(right-left+1):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        lp.next.next=curr
        lp.next=prev
        return dummy.next


        
        