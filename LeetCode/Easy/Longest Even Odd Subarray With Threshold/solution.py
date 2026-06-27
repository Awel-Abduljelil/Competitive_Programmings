class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_length = 0

        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                current_length = 1
                r = i

                while r + 1 < len(nums):
                    if nums[r+1] <= threshold and nums[r] % 2 != nums[r+1] % 2:
                        current_length += 1
                        r += 1
                    else:
                        break

                max_length = max(max_length, current_length)

        return max_length
