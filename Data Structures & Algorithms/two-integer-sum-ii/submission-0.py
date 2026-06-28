class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if i!=j:
                    if numbers[i]+numbers[j]==target:
                        return [numbers.index(numbers[i])+1, numbers.index(numbers[j])+1]