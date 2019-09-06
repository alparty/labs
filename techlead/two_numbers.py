"""
Hi, here's your problem today. This problem was recently asked by Microsoft:
You are given two linked-lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    if l1 or l2:
      a = l1.val if l1 else 0
      b = l2.val if l2 else 0
      n = c+a+b if a+b < 10 else a+b-10
      c = 0 if a+b<10 else 1
      node = ListNode(n)
      node.next = self.addTwoNumbers(l1.next if l1 else l1, l2.next if l2 else l2, c)
      return node
    return None if c==0 else ListNode(c)

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8