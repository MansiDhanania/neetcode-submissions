class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxa=0
        n=len(heights)
        for ind, height in enumerate(heights):
            start=ind
            while stack and height<stack[-1][0]:
                h, j=stack.pop()
                width=ind-j
                area=width*h
                maxa=max(maxa, area)
                start=j
            stack.append((height, start))
        while stack:
            h, j=stack.pop()
            w=n-j
            maxa=max(maxa, (w*h))
        return maxa