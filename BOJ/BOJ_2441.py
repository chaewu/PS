n = int(input()) # 히히 별찍기

for i in range(1, n + 1):
    print(" " * (i - 1) + "*" * (n + 1 - i))