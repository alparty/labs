"""
Given a sorted array, A, with possibly duplicated elements, find the 
indices of the first and last occurrences of a target element, x. 
Return -1 if the target is not found.
"""
class Solution: 
  def getRange(self, arr, target):
    ids = []
    for i in range(0, len(arr)):
      if arr[i] == target:
        ids.append(i)
    start = ids[0] if len(ids)>0 else -1
    end   = ids[len(ids)-1] if len(ids)>0 else -1
    ret = [start, end] if start-end!=0 else -1
    return ret
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

print(Solution().getRange([1,2,3], 5))