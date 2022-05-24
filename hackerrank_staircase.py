def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        for j in range(n, 0, -1):
            k = j - i
            print(" "*k, end="")
            print("#"*i)
            break


n = int(input().strip())

staircase(n)

