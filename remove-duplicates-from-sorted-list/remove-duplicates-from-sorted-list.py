# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        sentinel,start=ListNode(0,head),head
        while start and start.next:
            if start.val==start.next.val:
                temp=start.next
                start.next=temp.next
            else:
                start=start.next
        return sentinel.next
                
        
        