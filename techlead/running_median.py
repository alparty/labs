"""
You are given a stream of numbers. Compute the median for each new element .

Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]
"""

def running_median(stream):
  n = 0
  a = 0.0
  for i in stream:
    a = (a*n + i)/(n+1)
    n+=1
    print a,
  print

running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2