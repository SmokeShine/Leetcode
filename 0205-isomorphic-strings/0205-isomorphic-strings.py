class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s))!=len(set(t)) or len(s)!=len(t):
            return False
        dict_=collections.defaultdict(str)
        for x,y in zip(s,t):
            
            if y not in  dict_:
                dict_[y]=x
            elif dict_[y]!=x:
                return False
            
        
        return True 