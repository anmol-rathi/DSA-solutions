# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr=head
        while curr and curr.next:
            n=curr.next
            node=ListNode(gcd(curr.val,n.val))
            curr.next=node
            node.next=n
            curr=n
        return head
        