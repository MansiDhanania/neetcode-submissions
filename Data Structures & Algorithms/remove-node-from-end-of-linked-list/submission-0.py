# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rev(head: Optional[ListNode]):
            curr=head
            prev=None
            while curr is not None:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            return prev
        h=rev(head)
        prev=None
        count=1
        start=h
        while h is not None:
            if count==n:
                if prev is None:
                    start=h.next
                    return rev(start)
                else:
                    t=h.next
                    prev.next=t
                    h=t
                return rev(start)
            else:
                prev=h
                h=h.next
                count+=1
        return rev(start)