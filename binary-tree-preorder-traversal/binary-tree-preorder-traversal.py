# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer=[]
        self.dfs(root)
        return self.answer
    def dfs(self,root):
        if root is None:
            return root
        self.answer.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)