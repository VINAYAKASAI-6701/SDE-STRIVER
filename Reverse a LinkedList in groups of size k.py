# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #edge cases
        if head is None or k==1:
            return head
        dummy=ListNode(0)
        dummy.next=head

        curr=dummy
        nex=dummy
        prev=dummy
        c=0
        #calculate length of linked list
        while curr.next!=None:
            curr=curr.next
            c+=1
        #revese until it is greter than equa; to 3
        while c>=k:
            curr=prev.next
            nex=curr.next
            #do k-1 iterations
            for i in range(1,k):
                curr.next=nex.next
                nex.next=prev.next
                prev.next=nex
                nex=curr.next
            prev=curr
            c-=k
        return dummy.next

