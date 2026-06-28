class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p=[]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i!=j and nums[i]+nums[j]==target:
                    p.append(i)
                    p.append(j)
                    return(p)