nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [n for n in nums]
# print(my_list)

# my_list = [n*n for n in nums]
# print(my_list)

# my_list = list(map(lambda n: n*n, nums))
# print(my_list)
#
# x = "GeeksforGeeks"
# # lambda gets pass to print
# (lambda x: print(x))(x.upper())

my_list = [n*n for n in nums]
print(my_list)

my_list = [n % 2 == 0 for n in nums]
print(my_list)

my_list = [n for n in nums if n % 2 == 0]
print(my_list)



