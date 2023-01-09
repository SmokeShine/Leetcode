class Solution:
    def removeStars(self, s: str) -> str:
        if not s:
            return
        answer=[]
        stack=[]
        for i in s:
            if i!='*':
                stack.append(i)
            else:
                stack.pop()
        return ''.join(stack)