# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.answer=0
        self.dfs(root,-1)
        return self.answer
    def dfs(self,root,flag):
        if root is None:
            return root
        if root.left is None and root.right is None and flag==0:
            self.answer+=root.val            
        self.dfs(root.left,0)
        self.dfs(root.right,-1)
        