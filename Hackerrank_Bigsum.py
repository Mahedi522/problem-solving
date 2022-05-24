from functools import reduce


def aVeryBigSum(ar):
    sum = reduce(lambda a, b: a + b, ar)
    return sum

ar_count = int(input().strip())

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)
print(result)

