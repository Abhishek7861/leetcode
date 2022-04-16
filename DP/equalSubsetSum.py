# Get Sum of the arr
# If sum is odd return False
# else sum//2 is to be present in array to return true else false
# Use subsetSum solution to find this


class Solution:
    def __init__(self):
        self.T = []
        
    def init(self,sum,n):
        for i in range(n+1):
            row = []
            for j in range(sum+1):
                row.append(-1)
            self.T.append(row)
        
        
    def subSetSum(self, arr, Sum, n):
        if Sum == 0:
            self.T[n][Sum] = True
            return self.T[n][Sum]
        if n == 0 and Sum != 0:
            self.T[n][Sum] = False
            return self.T[n][Sum]
        if n == 0 and Sum == 0:
            self.T[n][Sum] = True
            return self.T[n][Sum]
        if self.T[n][Sum] != -1:
            return self.T[n][Sum]
        if arr[n - 1] <= Sum:
            self.T[n][Sum] = self.subSetSum(arr, Sum, n - 1) or self.subSetSum(arr, Sum - arr[n - 1], n - 1)
            return self.T[n][Sum]
        else:
            self.T[n][Sum] = self.subSetSum(arr, Sum, n - 1)
            return self.T[n][Sum]
        
    def canPartition(self, nums: List[int]) -> bool:
        arraySum = sum(nums)
        if arraySum % 2 == 1:
            return False
        else:
            self.init(arraySum//2,len(nums))
            return self.subSetSum(nums, arraySum // 2, len(nums))

    
