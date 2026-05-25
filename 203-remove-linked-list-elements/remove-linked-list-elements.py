# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr=head
        prev=None
        while(curr!=None):
            n=curr.next
            if(val==curr.val):
                if(curr==head):
                    head=n
                else:
                    prev.next=n
                curr.next=None
                curr=n
            else:
                prev=curr
                curr=n
        return head

        