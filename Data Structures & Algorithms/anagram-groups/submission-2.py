from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g=defaultdict(list)
        for i in strs:
            key="".join(sorted(i))
            g[key].append(i)
        return list(g.values())
