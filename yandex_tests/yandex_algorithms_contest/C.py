n = int(input())
if n != 0:
    a = int(input())
    ans = [a]
    for i in range(n-1):
        b = int(input())
        if b != a:
            ans.append(b)
            a = b
    print('--------')
    for el in ans:
        print(el)