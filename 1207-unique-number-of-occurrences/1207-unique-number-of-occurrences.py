class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_=collections.Counter(arr)
        return len(dict_)==len(set(dict_.values()))