class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set()
        vowels.add('a')
        vowels.add('e')
        vowels.add('i')
        vowels.add('o')
        vowels.add('u')
        if k==0:
            return 0
        left=0
        answer=0
        curr=0
        right=0
        count_=0
        for right in range(len(s)):
            if s[right] in vowels:
                count_+=1
            curr+=1
            
            while curr>k:
                if s[left] in vowels:
                    count_-=1
                left+=1
                curr-=1
            answer=max(answer,count_)
            
        return answer
    