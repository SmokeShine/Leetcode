# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_=math.inf
        stack=[root]
        ans=root.val
        while stack:
            node=stack.pop()
            if abs(node.val-target)<min_:
                min_=abs(node.val-target)
                ans=node.val
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ans
