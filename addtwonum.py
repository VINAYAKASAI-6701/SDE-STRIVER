# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, head1, head2):
        dummy_head=ListNode(-1)
        current=dummy_head
        t1=head1
        t2=head2
        carry=0
        while t1!=None or t2!=None:
            sum=carry
            if t1:
                sum+=t1.val
            if t2:
                sum+=t2.val
            new_node=ListNode(sum%10)
            carry=sum//10
            current.next=new_node
            current=current.next
            if t1:
                t1=t1.next
            if t2:
                t2=t2.next
        if carry:
            new_node=ListNode(carry)
            current.next=new_node
        return  dummy_head.next              
        
        