class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)

        if len(nums)==0:
            return 0
        else:
            i=0
            for j in range(len(nums)):
                if nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
    
                