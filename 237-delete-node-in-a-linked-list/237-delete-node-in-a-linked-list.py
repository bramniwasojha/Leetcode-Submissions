# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # add the next node's val in the given node then remove the next node
        node.val=node.next.val
        node.next=node.next.next