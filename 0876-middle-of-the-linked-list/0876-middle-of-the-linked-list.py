# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        fast=head
        slow=head        
        while fast and slow and fast.next:
            
            slow=slow.next
            fast=fast.next.next
            # fast=fast.next
        return slow