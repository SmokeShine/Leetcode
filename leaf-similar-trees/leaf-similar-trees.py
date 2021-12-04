# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        answer1=[]
        answer2=[]
        self.answer1=self.dfs(root1,answer1)
        self.answer2=self.dfs(root2,answer2)
        return self.answer1==self.answer2

    def dfs(self,root,answer):
        if root is None:
            return None
        if root.left is None and root.right is None:
            answer.append(root.val)
        self.dfs(root.left,answer)
        self.dfs(root.right,answer)
        return answer