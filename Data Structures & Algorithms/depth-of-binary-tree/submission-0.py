# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            d1=self.maxDepth(root.left)
            d2=self.maxDepth(root.right)
            depth=max(d1, d2)+1
            return depth
        return 0