class Solution(object):
    def twoSum(self, nums, target):
         hashmap={}
         for i in range(len(nums)):
                complement=target-nums[i]
                
                if complement in hashmap:
                    return [hashmap[complement], i]
                hashmap[nums[i]] = i
