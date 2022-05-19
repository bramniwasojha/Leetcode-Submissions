# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        flag=0
        while head!=None:
            if flag==1:
                curr=curr.next
                head=head.next
                flag=0
            else:
                head=head.next
                flag=1
        return curr