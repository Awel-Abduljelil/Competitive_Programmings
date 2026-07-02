class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        x = t
        for i in range(t):
            x -= 1
            num += 1
        x = num + t
        return x