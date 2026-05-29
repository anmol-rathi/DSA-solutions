# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=list1
        curr2=list2
        dummy_head=ListNode(-1,list1)
        head=dummy_head
        while(curr1!=None and curr2!=None):
            if(curr1.val<curr2.val):
                head.next=curr1
                head=curr1
                curr1=curr1.next
            else:
                head.next=curr2
                head=curr2
                curr2=curr2.next
        if(curr1!=None):
            head.next=curr1
        if(curr2!=None):
            head.next=curr2
        return dummy_head.next