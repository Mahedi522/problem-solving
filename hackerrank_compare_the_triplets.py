
def compareTriplets(a, b):
    al = 0
    bb = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            al += 1
        elif a[i] < b[i]:
            bb += 1
    c = [al, bb]
    return c


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))
result = compareTriplets(a, b)
print(result)

