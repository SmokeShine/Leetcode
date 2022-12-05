class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==1:
            return 1
        
        self.dict_={s[0]:0}
        
        best=1
        i=0
        j=1

        while j<len(s):
            if s[j] in self.dict_ and self.dict_.get(s[j],0)>=i:
                i=self.dict_[s[j]]+1
            else:
                best=max(best,j-i+1)
            
            
            self.dict_[s[j]]=j
            # print(best,self.dict_,j,i)
            
            j+=1
            
        
        return best
                
            