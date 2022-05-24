def countApplesAndOranges(s, t, a, b, apples, oranges):
    x = 0
    y = 0
    for i in apples:
        if s <= (a+i) <= t:
            x += 1
    for i in oranges:
        if s <= (b + i) <= t:
            y += 1
    print(x)
    print(y)


s = 7
t = 10
a = 4
b = 12
apples = [2, 3, -4]
oranges = [3, -2, -4]

countApplesAndOranges(s, t, a, b, apples, oranges)