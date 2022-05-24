a = 24
b = 60

# while True:
#     rem = n1 % n2
#     n1 = n2
#     n2 = rem
#     if rem == 0:
#         print("GCD is :", n1)
#         break


def gcd(n1, n2):
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
    if n1 > n2:
        return gcd(n1 % n2, n2)
    if n2 > n1:
        return gcd(n1, n2 % n1)


result = gcd(a, b)
print(result)
lcm = (a * b)/result
print("lcm is: ", lcm)

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


