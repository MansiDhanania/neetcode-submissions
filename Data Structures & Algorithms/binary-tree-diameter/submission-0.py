# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxd=0
        def getd(root):
            if root is None:
                return 0
            t1 = getd(root.left)
            t2 = getd(root.right)
            self.maxd=max(self.maxd, t1+t2)
            return max(t1, t2) + 1
        getd(root)
        return self.maxd