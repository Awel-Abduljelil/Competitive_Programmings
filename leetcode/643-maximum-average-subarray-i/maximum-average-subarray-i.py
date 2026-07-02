class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_k_element = sum(nums[:k])
        max_sum = sum_k_element
        for i in range(0,len(nums)-k):
            sum_k_element = sum_k_element - nums[i] + nums[k+i]
            max_sum = max(max_sum , sum_k_element)
        return max_sum/k