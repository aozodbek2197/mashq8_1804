# 1-mashq
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(a + b)
# 2-mashq
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(a & b)
# 3-mashq
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(a | b)
# 4-mashq
nums = list(map(int, input().split()))
print([i*2 for i in nums])
# 5-mashq
from collections import Counter

nums = list(map(int, input().split()))
print(Counter(nums).most_common(1))
