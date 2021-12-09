# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val>=list2.val:
                sentinel,start=ListNode(0,list2),ListNode(0,list2)
            else:
                sentinel,start=ListNode(0,list1),ListNode(0,list1)
            while list1 is not None or list2 is not None:
                if list1 is None and list2 is not None:
                    start.next=list2
                    break
                elif list2 is None and list1 is not None:
                    start.next=list1
                    break
                elif list1.val>=list2.val:
                    start.next=list2
                    list2=list2.next
                else:
                    start.next=list1
                    list1=list1.next
                start=start.next
            return sentinel.next
        elif list1:
            return list1
        elif list2:
            return list2
        return None