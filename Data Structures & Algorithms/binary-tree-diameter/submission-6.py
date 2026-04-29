# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0
        stack = [root]

        while stack:
            node = stack.pop()
            maxD = max(maxD, self.getDepth(node.left) + self.getDepth(node.right))

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return maxD 

    def getDepth(self, node):
        if not node:
            return 0

        return 1 + max(self.getDepth(node.left), self.getDepth(node.right))   