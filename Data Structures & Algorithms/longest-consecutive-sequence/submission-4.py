class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)))
        max_l=1
        curr_l=1
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1]==nums[i]+1:
                curr_l+=1
                if max_l<curr_l:
                    max_l=curr_l
            else:
                curr_l=1
        return max_l