N = int(input())

if N == 0:
    print("divide by zero")
    
else:
    numList = list(map(int, input().split()))
    res = sum(numList)/N / (sum(numList)/N)
    print("%.2f" % res)