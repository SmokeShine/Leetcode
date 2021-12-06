# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        pointer=head
        
        elements=[]
        while pointer :
            elements.append(pointer.val)
            pointer=pointer.next
        
        start=ListNode(elements.pop(-1),None)
        pointer=start
        while len(elements)>0:
            pointer.next=ListNode(elements.pop(-1),None)
            pointer=pointer.next
            

        return start