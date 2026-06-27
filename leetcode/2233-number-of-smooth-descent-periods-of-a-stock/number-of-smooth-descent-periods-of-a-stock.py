class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 1
        stock = 1

        for i in range(1, len(prices)):
            if prices[i-1] - prices[i] == 1:
                stock += 1
            else:
                stock = 1

            ans += stock

        return ans