class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for item in matrix:
            if target>item[-1]:
                continue
            else:
                return True if target in item else False
        return False