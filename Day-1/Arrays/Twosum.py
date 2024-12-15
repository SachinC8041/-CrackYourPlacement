class Solution:
    def twoSum(self, nums, target):
        hashset = dict()
        length = len(nums)
        for i in range(length):
            if target - nums[i] in hashset:
                return [i,hashset.get(target-nums[i])]
            hashset[nums[i]] = i 
        return []


        