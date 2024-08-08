# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. If not, return the 
# index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        num_len = len(nums)
        i = 0
        for i in range(i, num_len):
            print(nums[i], i)
            if nums[i] >= target:
                return i
        return 0 if num_len <= 1 and nums[-1] >= target else num_len
# Или вариант с бинарным деревом:
        # l = 0
        # r = len(nums) - 1
        # m = 0
        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return l    
  


nums = [1]
target = 2
x = Solution()
print(x.searchInsert(nums, target))