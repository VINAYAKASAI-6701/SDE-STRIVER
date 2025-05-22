class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        lm=height[0]
        rm=height[0]
        l=[]
        r=[]
        #left arr formed
        for i in height:
            if i>lm1:
                lm1=i
            l.append(lm1)
        #right arr
        for i in reversed(height):
            if i>rm:
                rm=i
            r.append(rm)
        r.reverse()
        #water content is min(lm[i],rm[i])-arr[i]
        s=0
        for i in range(n):
            s+=min(l[i],r[i])-height[i]
        return s
