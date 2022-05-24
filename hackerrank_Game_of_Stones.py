def gameOfStones(num):
    a = "First"
    b = "Second"
    if num % 7 < 2:
        return b
    else:
        return a


t = int(input().strip())

for t_itr in range(t):
    n = int(input().strip())
    result = gameOfStones(n)

    print(result)
