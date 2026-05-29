# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        curr=head
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        prev=None
        while(slow!=None):
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        while(prev!=None):
            if(prev.val!=curr.val):
                return False
            prev=prev.next
            curr=curr.next
        return True
        