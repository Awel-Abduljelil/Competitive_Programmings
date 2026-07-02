class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        lst = sorted(nums)
        l = 0
        r = len(nums)-1
        max_sum = lst[0]+lst[-1]
        while l < r:
            s = lst[l] + lst[r]
            max_sum = max(s,max_sum)
            l += 1
            r -= 1
        return max_sum