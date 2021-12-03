# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.queue=[]
        return self.bfs(root)
    def bfs(self,root):
        if root is None:
            return False
        self.queue.append(root)
        test=root.val
        while len(self.queue)>0:
            element=self.queue.pop(0) 
            if element.val!=test:
                return False
            if element.left:
                self.queue.append(element.left)
            if element.right:
                self.queue.append(element.right)
                        
        return True
        