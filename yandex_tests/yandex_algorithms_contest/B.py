n = int(input())
nums = [int(input()) for i in range(n)]
print(nums)
i, best = 0, 0
for el in nums:
    if el == 1:
        i += 1
        best = max(best, i)
    else:
        i = 0
print(best)