# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head  is None or head.next is None or k==0:
            return head
        #compute the length
        c=1
        curr=head
        while curr.next:
            c+=1
            curr=curr.next
        #go till the last node and point last node to first make it circular
        curr.next=head
        k=k%c
        k=c-k
        while k:
            curr=curr.next
            k-=1
        #make the node head and break connection
        head=curr.next
        curr.next=None
        return head
