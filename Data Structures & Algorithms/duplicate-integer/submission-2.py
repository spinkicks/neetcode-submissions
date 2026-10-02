class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0:
            return False
        dic ={}
        dic[nums[0]] = nums[0]
        for i in range(1, n):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]] = nums[i]
        return False