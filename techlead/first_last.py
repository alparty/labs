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
    end   = ids[len(ids)-1] if len(ids)>1 else start
    ret = [start, end]
    return ret if start != -1 and end != -1 else -1
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x) == [1,4])
print(Solution().getRange([1,1,2,1,5], 1) == [0,3])
print(Solution().getRange([1,2,5], 2) == [1,1])
print(Solution().getRange([1,2,5], 7) == -1)
print(Solution().getRange([], 7) == -1)