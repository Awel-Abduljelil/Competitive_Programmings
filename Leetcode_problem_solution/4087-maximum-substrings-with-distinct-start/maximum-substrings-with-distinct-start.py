class Solution:
    def maxDistinct(self, s: str) -> int:
        string_to_set = set(s)
        return len(string_to_set)
