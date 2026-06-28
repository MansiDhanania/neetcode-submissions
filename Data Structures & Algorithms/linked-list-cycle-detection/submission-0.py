# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr=head
        vis=[]
        while curr is not None:
            if curr not in vis:
                vis.append(curr)
                curr=curr.next
            else:
                return True
        return False