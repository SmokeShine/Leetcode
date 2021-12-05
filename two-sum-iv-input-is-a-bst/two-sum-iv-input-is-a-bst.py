# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.nodes=set()
        self.dfs(root)
        print(self.nodes)
        for x in self.nodes:
            if k-x in self.nodes and x!=k-x:
                return True
        return False
    def dfs(self,root):
        if root is None:
            return root
        self.nodes.add(root.val)
        self.dfs(root.left)
        self.dfs(root.right)