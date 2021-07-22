cities = int(input())
xy = []
for city in range(1, cities + 1):
    xy.append([city, input().split(' ')])
print(xy)
print(*xy)
dictt = {}