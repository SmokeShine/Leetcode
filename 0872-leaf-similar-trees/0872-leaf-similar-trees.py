class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        val1=self.dfs(root1)
        val2=self.dfs(root2)
        #print(val1,val2)
        return val1==val2
    def dfs(self,root):
        leaf_nodes=[]
        stack=[]
        stack.append(root)
        while stack:
            node=stack.pop()
            if not node.left and not node.right:
                leaf_nodes.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return leaf_nodes