s = input()
l = list(s)
a = 0
b = 0
c = 0
d = 0
e = 0
for i in range(len(l)):

    def show(s):
        if s:
            print("True")
        else:
            print("False")


    if a == 0:
        if l[i].isalnum():
            a += 1

    if b == 0:
        if l[i].isalpha():
            b += 1

    if c == 0:
        if l[i].isdigit():
            c += 1

    if d == 0:
        if l[i].islower():
            d += 1

    if e == 0:
        if l[i].isupper():
            e += 1
if a == 1:
    print("True")
else:
    print("False")
if b == 1:
    print("True")
else:
    print("False")
if c == 1:
    print("True")
else:
    print("False")
if d == 1:
    print("True")
else:
    print("False")
if e == 1:
    print("True")
else:
    print("False")
