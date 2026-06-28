class Solution:
    def trap(self, height: List[int]) -> int:
        l=[]
        r=[]
        maxl=0
        maxr=0
        water=0
        for i in range(len(height)):
            l.append(maxl)
            r.append(maxr)
            if height[i]>maxl:
                maxl=height[i]
            if height[len(height)-1-i]>maxr:
                maxr=height[len(height)-1-i]
        r.reverse()
        for i in range(len(l)):
            w=min([l[i], r[i]])-height[i]
            if w>0:
                water=water+w
        return water