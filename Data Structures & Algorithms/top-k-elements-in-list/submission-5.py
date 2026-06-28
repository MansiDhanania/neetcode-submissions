from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=defaultdict(int)
        nums=sorted(nums)
        vis=defaultdict(int)
        for item in nums:
            if item in vis.keys():
                vis[item]=vis[item]+1
            else:
                vis[item]=1
        sor = dict(sorted(vis.items(), key=lambda item: item[1], reverse=True))
        kk = list(sor.keys())
        vv = list(sor.values())
        ans=[]
        for i in range(len(vv)):
            if i<k:
                ans.append(kk[i])
        return ans