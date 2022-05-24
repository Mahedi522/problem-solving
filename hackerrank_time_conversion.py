def timeConversion(s):
    t = s[0:2]
    if s.find("PM") > 0 and t != "12":
        t = str(12 + int(s[0:2]))

    if s.find("AM") > 0 and t == "12":
        t = "00"

    s = t + s[2:-2]

    return s


s = "08:45:50PM"
result = timeConversion(s)
print(result)


# m = s[-2:]
# if m == "PM" and s[:2] != "12":
#     s = str(12 + int(s[0:2])) + s[2:]
# print(s)
