# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        temp=ListNode()
        head=temp
        while list1 and list2:
            if list1.val>=list2.val:
                temp.next=list2
                list2=list2.next                
            else:
                temp.next=list1
                list1=list1.next
            temp=temp.next
        while list1:
            temp.next=list1
            temp=temp.next
            list1=list1.next
        while list2:
            temp.next=list2
            temp=temp.next
            list2=list2.next
            
        return head.next
            