class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        l = len(nums)
        for i in range(l):
            dic[nums[i]] = dic.get(nums[i], 0) + 1
        
        sorted_items = sorted(dic.items(), key=lambda item: item[1], reverse=True)
        result = [None]*k
        for i in range(k):
            result[i] = sorted_items[i][0]
        return result


        