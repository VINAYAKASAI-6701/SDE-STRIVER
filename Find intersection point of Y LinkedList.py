class Solution:
    def intersectPoint(self, head1, head2):
        if not head1 or not head2:
            return None
        
        d1 = head1
        d2 = head2
        
        while d1 != d2:
            d1 = d1.next if d1 else head2
            d2 = d2.next if d2 else head1
            
        return d1  # Return the Node, not its data
