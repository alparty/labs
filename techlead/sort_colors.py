"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Can you do this in a single pass?

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""

class Solution:
  def sortColors(self, nums):
    vals = [0,0,0]
    for i in range(len(nums)):
      vals[nums[i]] += 1
    numsort = ([0]*vals[0]) + ([1]*vals[1]) + ([2]*vals[2])

    return numsort

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
      #[0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

numsort = Solution().sortColors(nums)
# print(numsort)
print(numsort == [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2])

print(Solution().sortColors([2,0,2,1,1,0]) == [0,0,1,1,2,2])
print(Solution().sortColors([0]) == [0])
print(Solution().sortColors([1]) == [1])
print(Solution().sortColors([]) == [])