# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        # head=ListNode()
        temp=head=ListNode()
        
        while l1 and l2:
            sum_=l1.val+l2.val+carry
            val=sum_%10
            carry=sum_//10
            temp.next=ListNode(val)
            l1=l1.next
            l2=l2.next
            temp=temp.next
            
        while l1:
            sum_=l1.val+carry
            val=sum_%10
            carry=sum_//10
            temp.next=ListNode(val)
            l1=l1.next
            temp=temp.next
            
        while l2:
            sum_=l2.val+carry
            val=sum_%10
            carry=sum_//10
            temp.next=ListNode(val)
            l2=l2.next
            temp=temp.next
            
        if carry>0:
            temp.next=ListNode(carry)
            
        
        return head.next