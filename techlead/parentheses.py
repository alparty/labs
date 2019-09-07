"""
Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:

Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False
"""
class Solution:
  def isValid(self, s):
    stack = []
    openB = ['(', '[', '{']
    closeB = {'(':')', '[':']', '{':'}'}

    for i in range(len(s)):
      c = s[i]
      if c in openB:
        stack.insert(0, c)
      else:
        p = stack.pop(0)
        if c != closeB[p]:
          return False
        
    return len(stack) == 0

# Test Program
s = "()(){(())" 
print(Solution().isValid(s) == False)

s = ""
print(Solution().isValid(s) == True)

s = "([{}])()"
print(Solution().isValid(s) == True)

s = "({([{}()][()])})(((([](){()}))))"
print(Solution().isValid(s) == True)