# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return
        slow=head
        fast=head
        if not head.next:
            return None
        for _ in range(n) :   
            fast=fast.next
        temp=head
        c=0
        while temp:
            temp=temp.next
            c+=1
        if n==c:
            return head.next
        while slow and fast and fast.next :
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head
            
        