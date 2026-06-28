# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1=ListNode(-1)
        l2=ListNode(-1)
        slow=head
        fast=head.next
        l1=slow
        l2=fast
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l2=slow.next
        slow.next=None
        h=l2
        prev=None
        while h is not None:
            aft=h.next
            h.next=prev
            prev=h
            h=aft
        curr=l1
        while curr and prev:
            temp=curr.next
            te=prev.next
            curr.next=prev
            prev.next=temp
            curr=temp
            prev=te
        return prev