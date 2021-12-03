# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.answer=[]
        self.dfs(root)
        start=self.answer.pop(0)
        temp=TreeNode(start)
        tree_answer=temp
        while len(self.answer)>0:
            next_=self.answer.pop(0)
            temp.right=TreeNode(next_)
            temp=temp.right
        return tree_answer  
    def dfs(self,root):
        if root is None:
            return None
        self.dfs(root.left)
        self.answer.append(root.val)        
        self.dfs(root.right)
        