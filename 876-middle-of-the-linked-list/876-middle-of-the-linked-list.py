# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        while head!=None and head.next!=None and head.next.next!=None:
            curr=curr.next
            head=head.next.next
        if head.next!=None and head.next.next==None:
            curr=curr.next
        return curr