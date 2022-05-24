def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x1 >= x2:
        g = x1
        v3 = v1
        v4 = v2
        l = x2
    else:
        g = x2
        v3 = v2
        v4 = v1
        l = x1

    for i in range(10000):
        # print(g, "g")
        # print(v1,"v1")
        g = g + v3
        l = l + v4

        # print(g, "g")
        # print(l, "l")

        if g == l :
            s = "YES"
            return s

        if l > g:
            s = "NO"
            return s
        if i == 9999:
            s = "NO"
            return s


x1 = 0
v1 = 2
x2 = 5
v2 = 3

print(kangaroo(x1, v1, x2, v2))
