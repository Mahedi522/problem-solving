def miniMaxSum(arr):
    # Write your code here
    x = 0
    y = 0
    arr.sort()
    for i in range(len(arr)-1):
        x = x + arr[i]
        y = y + arr[i+1]
    print(x, y, sep=" ")


arr = list(map(int, input().rstrip().split()))

miniMaxSum(arr)