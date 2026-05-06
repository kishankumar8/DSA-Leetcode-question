class Solution(object):
    def twoSum(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={}
        for i in range(len(num)):
            complement=target-num[i]

            if complement in hashmap:
                return

                [hashmap[complement],i]
                hashmap[nums[i]]=i
