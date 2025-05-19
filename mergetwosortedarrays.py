class Solution:
    def swapifgreater(self, a, b, ind1, ind2):
        if a[ind1] > b[ind2]:
            a[ind1], b[ind2] = b[ind2], a[ind1]

    def mergeArrays(self, a, b):
        n = len(a)
        m = len(b)
        k = n + m
        gap = (k // 2) + (k % 2)  # ceil of k/2

        while gap > 0:
            left = 0
            right = left + gap

            while right < k:
                # both in a
                if left < n and right < n:
                    self.swapifgreater(a, a, left, right)
                # left in a, right in b
                elif left < n and right >= n:
                    self.swapifgreater(a, b, left, right - n)
                # both in b
                else:
                    self.swapifgreater(b, b, left - n, right - n)

                left += 1
                right += 1

            if gap == 1:
                break
            gap = (gap // 2) + (gap % 2)  # ceil of gap/2
