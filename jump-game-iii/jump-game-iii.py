class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        stack=[start]
        seen=set()
        len_=len(arr)-1
        while stack:
            node=stack.pop()
            if arr[node]==0:
                return True
            if node in seen:
                continue
            seen.add(node)
            if node+arr[node]<=len_:
                stack.append(node+arr[node])
            if node-arr[node]>=0:
                stack.append(node-arr[node])
        
        return False