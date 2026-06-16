class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = target[0]
        for i in range(1, len(target)):
            if target[i] <= target[i - 1]:
                continue
            else:
                result += target[i] - target[i - 1]

        return result