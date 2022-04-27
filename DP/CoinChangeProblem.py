# https://leetcode.com/submissions/detail/687986260/
# Return Min number of coins needed for given amount


import math


class Solution:
    def __init__(self):
        self.T = []
        for i in range(13):
            row = []
            for j in range(10001):
                row.append(-1)
            self.T.append(row)

    def coinChange(self, coins, amount: int) -> int:
        self.CCP(coins, amount, len(coins))
        if self.T[len(coins)][amount] == math.inf:
            return -1
        else:
            return self.T[len(coins)][amount]

    def CCP(self, coin, amount, n):
        if self.T[n][amount] != -1:
            return self.T[n][amount]
        if amount == 0:
            self.T[n][amount] = 0
            return self.T[n][amount]
        elif n == 0 and amount != 0:
            self.T[n][amount] = math.inf
            return self.T[n][amount]
        elif coin[n - 1] <= amount:
            self.T[n][amount] = min(1 + self.CCP(coin, amount - coin[n - 1], n), self.CCP(coin, amount, n - 1))
            return self.T[n][amount]
        else:
            self.T[n][amount] = self.CCP(coin, amount, n - 1)
            return self.T[n][amount]


obj = Solution()
print(obj.coinChange([3,7,405,436], 8839))

#
# [3,7,405,436]
# 8839
