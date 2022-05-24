def diagonalDifference(arr):
    x = 0
    y = 0
    for i in range(len(arr)):
        for j in reversed((range(0, len(arr)))):
            a = j-i
            y = y + arr[i][a]
            x = x + arr[i][i]
            break
    if x > y:
        return x-y
    else:
        return y-x


n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)
