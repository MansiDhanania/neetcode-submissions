from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def isAna(string1, string2):
        #     if len(string1)==len(string2):
        #         s1=sorted(list(string1))
        #         s2=sorted(list(string2))
        #         if s1==s2:
        #             # is anagram!
        #             return True
        # l=[]
        # visited=[]
        # for i in range(len(strs)):
        #     p=[]
        #     p.append(strs[i])
        #     visited.append(i)
        #     for j in range(i+1, len(strs)):
        #         if i!=j and j not in visited and isAna(p[0], strs[j])==True:
        #             p.append(strs[j])
        #             visited.append(j)
        #         else:
        #             pass
        #     l.append(p)
        # return(l)

        g=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            g[key].append(i)
        return list(g.values())
