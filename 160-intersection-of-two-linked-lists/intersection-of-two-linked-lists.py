# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        h={}
        while headB:
            h[headB]=headB.val
            headB=headB.next
        while headA:
            if headA in h:
                return headA
            headA=headA.next
        return None
        