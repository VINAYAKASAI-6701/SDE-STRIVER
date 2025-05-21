class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        temp = head
        while temp:
            if temp in seen:
                return temp  # Start of the cycle
            seen.add(temp)
            temp = temp.next
        return None  # No cycle
