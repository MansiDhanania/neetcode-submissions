class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m=0
        left=0
        right=len(heights)-1
        while left<right:
            p=(right-left)*min([heights[left], heights[right]])
            if m<p:
                m=p
            if heights[left]<heights[right]:
                left=left+1
            else:
                right=right-1
        return m