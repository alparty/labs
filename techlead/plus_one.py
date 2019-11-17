"""Given a non-empty array where each element represents a digit of a non-negative integer, 
  add one to the integer. The most significant digit is at the front of the array and 
  each element in the array contains only one digit. Furthermore, the integer does not 
  have leading zeros, except in the case of the number '0'.

Example:

Input: [2,3,4]
Output: [2,3,5]
"""
class Solution():
  def plusOne(self, digits):
    plus = 1
    for i in xrange(len(digits)-1, -1, -1):
      digits[i] += plus
      if digits[i] >= 10:
        digits[i] = 0
        plus = 1
      else:
        plus = 0
        break
    if(plus>0):
      digits.insert(0,plus)
    return digits

print(Solution().plusOne([2,3,4]) == [2,3,5])
print(Solution().plusOne([2,9,9]) == [3,0,0])
print(Solution().plusOne([9]) == [1,0])
print(Solution().plusOne([0]) == [1])
