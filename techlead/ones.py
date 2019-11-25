"""Return the longest run of 1s for a given integer n's binary representation.

Example:

Input: 242
Output: 4

242 in binary is 0b11110010, so the longest run of 1 is 4.
"""

def longest_run(n): 
  return max(map(len, str(bin(n))[2:].split('0')))


print(longest_run(242) == 4)
print(longest_run(0) == 0)
print(longest_run(1) == 1)
print(longest_run(2) == 1)
print(longest_run(3) == 2)
print(longest_run(128) == 1)
# 4