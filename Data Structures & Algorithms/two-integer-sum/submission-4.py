class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] in dic:
                return [dic.get(nums[i]), i]
            else:
                dic[target-nums[i]] = i