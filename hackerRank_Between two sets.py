import math
#
# li1 = [2, 4]
# li2 = [16, 32, 96]
#
# gc = math.gcd(li2[0], li2[1])
# print(gc)
#
#
# def find_gcd(x, y):
#     while (y):
#         x, y = y, x % y
#
#     return x
#
#
# l = [2, 4, 6, 8, 16]
#
# num1 = l[0]
# num2 = l[1]
# gcd = find_gcd(num1, num2)
#
# for i in range(2, len(l)):
#     gcd = find_gcd(gcd, l[i])
#
# print(gcd)


def FindGcd(lst):
    def find_gcd(n1, n2):
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        if n1 == n2:
            return n1

        if n1 > n2:
            return find_gcd(n1 % n2, n2)
        if n2 > n1:
            return find_gcd(n1, n2 % n1)

    gcd = find_gcd(lst[0], lst[1])

    for i in range(2, len(lst)):
        gcd = find_gcd(gcd, lst[i])
    return gcd


def find_gcd1(n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 == n2:
        return n1

    if n1 > n2:
        return find_gcd1(n1 % n2, n2)
    if n2 > n1:
        return find_gcd1(n1, n2 % n1)


li = [42, 84]
li.sort()
print(li)
if len(li)== 1:
    gcd1 = li[0]
else:
    gcd1 = FindGcd(li)
print("gcd :", gcd1)

li1 = [2, 3, 6]
if len(li1) == 1:
    lcm1 = li1[0]
if len(li1) > 1:
    print("fun")
    gcd2 = find_gcd1(li1[0], li1[1])
    print("gcd2:",gcd2)
    lcm = (li1[0]*li1[1])/gcd2
    lcm1 = lcm
    if len(li1) >= 2:
        for i in range(2, len(li1)):
            z = lcm
            lcm = find_gcd1(lcm, li1[i])
            lcm1 = (z*li1[i])/lcm

print("lcm :", lcm1)
multiple = 0
y = 0

while multiple <= gcd1:
    multiple += lcm1
    if gcd1 % multiple == 0:
        y += 1
    if multiple > gcd1:
        break
print("result:", y)
