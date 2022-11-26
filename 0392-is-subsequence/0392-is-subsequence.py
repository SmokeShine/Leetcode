class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<=len(s)-1 and j<=len(t)-1:
            if s[i]==t[j]:
                i+=1
                
            j+=1
        if i==len(s):
            return True
        return False
            