class Solution:
    def reverseVowels(self, s: str) -> str:
        i=0
        j=len(s)-1
        vowels=set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')
        s_=[x for x in s]
        while i<j:
            if s_[i].lower() in vowels and s_[j].lower() in vowels:
                s_[i],s_[j]=s_[j],s_[i]
                i+=1
                j-=1
                
            elif s_[i].lower() in vowels:
                j-=1
            elif s_[j].lower() in vowels:
                i+=1
            else:
                i+=1
                j-=1
            
        return ''.join(s_)