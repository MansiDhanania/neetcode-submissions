class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        p=False
        if len(s)==len(t):
            ss = list(s)
            tt = list(t)
            if sorted(ss)==sorted(tt):
                p=True
        return(p)