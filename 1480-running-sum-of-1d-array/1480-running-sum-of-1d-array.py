class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        runningSum = 0
        for i in nums:
            runningSum += i
            result.append(runningSum)
        return result