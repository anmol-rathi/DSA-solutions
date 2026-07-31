# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        node=head
        count=0
        while slow:
            slow=slow.next
            count+=1
        print(count)
        a=count-n
        print(a)
        if a==0:
            return head.next
        for i in range(a-1):
            node=node.next
        if node.next:
            node.next=node.next.next
            return head
        return None
            

        