class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dicLeft = {}
        dicRight = {}
        runningRight = 1
        runningLeft = 1
        result = []
        l = len(nums)
        for i in range(l):
            dicLeft[i] = runningLeft
            dicRight[l - 1 - i] = runningRight
            runningLeft = runningLeft * nums[i]
            runningRight = runningRight * nums[l - 1 - i]
            
        for i in range(l):
            result.append(dicLeft[i]*dicRight[i])

        return result