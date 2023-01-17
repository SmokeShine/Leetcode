# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.answer=[]
        return self.dfs(root)

    def dfs(self,root):
        if not root:
            return []
        left,right=[],[]
        if root.left:
            left=self.dfs(root.left)
        if root.right:
            right=self.dfs(root.right)
        return left+[root.val]+right
        
        
        
        
        
        
        
        