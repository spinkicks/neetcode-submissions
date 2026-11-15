class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        result = [1] * l
        runningLeft = 1
        runningRight = 1
        
        for i in range(l):
            result[i] *= runningLeft
            runningLeft *= nums[i]
            
            result[l - 1 - i] *= runningRight
            runningRight *= nums[l - 1 - i]
            
        return result