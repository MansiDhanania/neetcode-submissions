class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        warmer=[0]*(len(temperatures))
        for i in range(len(temperatures)):
            count=1
            for j in range(i+1, len(temperatures)):
                if i!=j and temperatures[j]>temperatures[i]:
                    warmer[i]=count
                    break
                elif i!=j and temperatures[j]<=temperatures[i]:
                    count+=1
        return warmer