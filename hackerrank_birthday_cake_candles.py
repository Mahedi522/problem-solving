def birthdayCakeCandles(candles):
    m = (max(candles))
    x = 0
    for i in candles:
        if i == m:
            x += 1
        else:
            continue
    return x


candles_count = int(input().strip())

candles = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(candles)
print(result)
