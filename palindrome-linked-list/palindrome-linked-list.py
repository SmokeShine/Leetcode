# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        slow,fast=head,head
        while fast and fast.next:
            stack.append(slow.val)
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        
        while slow and len(stack)>0:            
            check=stack.pop(-1)
            
            if check!=slow.val:
                return False
            slow=slow.next
        return True