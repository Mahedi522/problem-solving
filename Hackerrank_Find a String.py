def count_substring(string, sub_string):
    a = 0
    b = 0
    i = 0
    while i < len(string):
        for j in range(0, len(sub_string)):
            if string[i] == sub_string[j]:
                a += 1

                if len(sub_string) == a:
                    b += 1
                    a = 0
                    i = i - 1
                break
        i = i + 1
    return b


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = "abcdcdc"
    sub_string = "cdc"
    count = count_substring(string, sub_string)
    print(count)


# def count_substring(string, sub_string):
#     count = 0
#     for i in range(0, len(string) - len(sub_string) + 1):
#         l = i
#         for j in range(0, len(sub_string)):
#             if string[l] == sub_string[j]:
#                 l += 1
#                 if j == len(sub_string) - 1:
#                     count = count + 1
#                 else:
#                     continue
#             else:
#                 break
#
#     return count
