li = []
def round(x):
    for i in l:
        if (i + 1) % 5 == 0 and i > 37:
            i = i+1

        if (i + 2) % 5 == 0 and i > 37:
            i = i+2

        li.append(i)
    return li

l = [44, 84, 94, 21]

result = round(l)
print(result)

# n = int(input())
# for i in range(n):
#     x = int(input())
#     result = round(x)
#     print(result)
