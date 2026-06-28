class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub=""
        maxl=0
        le=0
        for i in range(len(s)):
            if s[i] not in sub:
                sub=sub+s[i]
                le+=1
                if maxl<le:
                    maxl=le
            else:
                sub=sub+s[i]
                if maxl<le:
                    maxl=le
                sub=sub[sub.find(s[i])+1:]
                le=len(sub)
        return maxl