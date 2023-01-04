class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if not s:
            return
        i=0
        j=len(s)-1
        s_=[x for x in s]
        while i<j:
            if s_[i].isalpha() and s_[j].isalpha():
                s_[i],s_[j]=s_[j],s_[i]
                i+=1
                j-=1
            elif not s_[i].isalpha():
                i+=1
            else:
                j-=1
        return ''.join(s_)
            
        