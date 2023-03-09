# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a=self.reverse_(l1)
        b=self.reverse_(l2)
        c= self.add_(a,b)
        return self.reverse_(c)
    def reverse_(self,head):
        if not head or not head.next:
            return head
        p = self.reverse_(head.next)
        head.next.next=head
        head.next=None
        return p
    def add_(self,list1,list2):
        head=ListNode(0)
        curr=head
        carry=0
        while list1 and list2:
            # print(list1.val,list2.val)

            val=(list1.val+list2.val+carry)%10
            carry=(list1.val+list2.val+carry)//10
            list1=list1.next
            list2=list2.next
            temp=ListNode(val)
            # print(temp.val)
            curr.next=temp
            curr=curr.next
            
        while list1:
            # print(list1.val)
            val=(list1.val+carry)%10
            carry=(list1.val+carry)//10
            list1=list1.next
            temp=ListNode(val)
            # print(temp.val)
            curr.next=temp
            curr=curr.next

        while list2:
            # print(list2.val)
            val=(list2.val+carry)%10
            carry=(list2.val+carry)//10
            list2=list2.next
            temp=ListNode(val)
            # print(temp.val)
            curr.next=temp
            curr=curr.next
        
        if carry>0:
            curr.next=ListNode(carry)
        return head.next
            