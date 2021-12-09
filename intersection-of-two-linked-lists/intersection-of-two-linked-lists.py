# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_a=0
        len_b=0
        headA_copy=headA
        headB_copy=headB
        while headA_copy:
            len_a+=1
            headA_copy=headA_copy.next
        while headB_copy:
            len_b+=1
            headB_copy=headB_copy.next
        diff=abs(len_a-len_b)
        if len_a>len_b:
            while diff!=0:
                headA=headA.next
                diff-=1
        else:
            while diff!=0:
                headB=headB.next
                diff-=1
        while headA and headB:
            if headA==headB:
                return headA
            else:
                headA=headA.next
                headB=headB.next
        return None
            