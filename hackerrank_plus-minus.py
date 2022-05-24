def plusMinus(arr):
    p = 0
    n = 0
    z = 0
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    l = len(arr)
    x = p/l
    y = n/l
    v = z/l
    print("{:.6f}".format(x))
    print("{:.6f}".format(y))
    print("{:.6f}".format(v))


n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
