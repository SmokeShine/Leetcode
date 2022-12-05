class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_=Counter(magazine)
        r_=Counter(ransomNote)
        # print(m_)
        # print(r_)
        for i in r_:
            if i not in m_:
                return False
            elif m_[i]<r_[i]:
                return False
        return True