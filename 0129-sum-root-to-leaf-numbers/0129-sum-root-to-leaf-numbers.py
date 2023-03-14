# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=[(root,root.val)]
        ans=0
        while stack:
            node,val = stack.pop()
            if not node.left and not node.right:
                ans+=val
            if node.left:
                c = 10*val + node.left.val
                stack.append((node.left,c))
            if node.right:
                c = 10*val + node.right.val
                stack.append((node.right,c))
                
        return ans