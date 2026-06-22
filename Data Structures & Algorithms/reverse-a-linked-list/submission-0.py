# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            # take the next and make it prev but store curr.next because you don't want to lose it
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev