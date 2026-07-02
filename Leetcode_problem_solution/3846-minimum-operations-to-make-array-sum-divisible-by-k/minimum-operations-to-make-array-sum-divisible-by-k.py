class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr_sum = sum(nums)
        count = 0
        while not arr_sum%k == 0:
            arr_sum -= 1
            count += 1
        return count
