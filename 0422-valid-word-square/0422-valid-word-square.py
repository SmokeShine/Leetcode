class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:
            return False
        words_=[list(x) for x in words]
        words__=[list(x) for x in itertools.zip_longest(*words_,fillvalue='')]
        return [''.join(x) for x in words__] == [''.join(x) for x in words_]