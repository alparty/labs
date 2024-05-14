""" Given a string, you need to reverse the order of characters in each word 
within a sentence while still preserving whitespace and initial word order.
"""

class Solution:
	def reverseWords(self, s):
		acc = ""
		elem = ""
		for i in range(len(s)):
		    if s[i]!=' ':
		        elem = s[i]+elem
		    else:
		        acc = acc + elem + " "
		        elem=""
		acc = acc+elem
		return acc

print(Solution().reverseWords("The cat is in the hat")=="ehT tac si ni eht tah")
print(Solution().reverseWords("")=="")
print(Solution().reverseWords("a")=="a")
