class Solution:
    def removeVowels(self, s: str) -> str:
        c=['a','e','i','o','u']
        if not s:
            return
        return ''.join(x for x in s if x not in c)