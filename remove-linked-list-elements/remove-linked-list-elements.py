# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head
        sentinel=temp=ListNode(0,head)
        
        while temp.next:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return sentinel.next