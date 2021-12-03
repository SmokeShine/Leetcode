# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.answer=[]
        self.dfs(root,"")
        print(self.answer)
        return self.answer
    def dfs(self,root,current_path):
        if root is None:
            return root
        current_path=current_path+"->"+str(root.val)
        if root.left is None and root.right is None:
            self.answer.append(current_path[2:])
        self.dfs(root.left,current_path)
        self.dfs(root.right,current_path)
        