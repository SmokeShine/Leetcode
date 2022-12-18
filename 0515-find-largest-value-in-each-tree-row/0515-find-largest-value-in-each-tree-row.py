# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=collections.deque([(root,0)])
        answer=collections.defaultdict()
        answer[0]=root.val
        while queue:
            node,level=queue.popleft()
            if node.left:
                queue.append([node.left,level+1])
                if answer.get(level+1,-math.inf)<node.left.val:
                    answer[level+1]=node.left.val
            if node.right:
                queue.append([node.right,level+1])
                if answer.get(level+1,-math.inf)<node.right.val:
                    answer[level+1]=node.right.val
            
        return answer.values()