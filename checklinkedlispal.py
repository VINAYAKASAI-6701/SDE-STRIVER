# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev(self,head):
        temp=head
        back=None
        if temp is None or temp.next is None:
            return head
        while temp!=None:
            front=temp.next
            temp.next=back
            back=temp
            temp=front
        return back        
        
    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next
        new_head=self.rev(slow.next)    
        first=head
        second=new_head
        while second!=None:
            if first.val!=second.val:
                self.rev(new_head)
                return False
            first=first.next
            second=second.next
        self.rev(new_head)
        return True        
    
    """
    :type head: Optional[ListNode]
    :rtype: bool
    """
    