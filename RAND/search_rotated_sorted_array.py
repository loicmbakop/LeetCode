class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2

            if nums[middle] == target:
                return middle
            
            if nums[left] <= nums[middle]: # left side is sorted
                if nums[left] <= target < nums[middle]:
                    right = middle -1
                else: 
                    left = middle +1
            
            else:# right side is sorted
                if nums[middle] < target <= nums[right]: 
                    left = middle +1
                else:
                    right = middle -1
        return -1

