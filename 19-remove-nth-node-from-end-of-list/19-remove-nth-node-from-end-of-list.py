# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        l = 0
        while current != None:
            l += 1
            current = current.next
        ind = l - n
        if ind == 0:
            return head.next
        current = head
        prev = None
        i=0
        while current != None:
            if i == ind:
                prev.next=current.next
                current=None
                break
            i+=1
            prev = current
            current = current.next
        return head