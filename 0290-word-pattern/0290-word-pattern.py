class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict_=collections.defaultdict(str)
        for x,y in itertools.zip_longest(pattern,s.split()):
            
            if y not in dict_:
                dict_[y]=x
            elif dict_[y]!=x:                
                return False
            
        return True if len(set(pattern))==len(set(s.split())) else False