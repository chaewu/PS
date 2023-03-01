n = int(input())

for i in range(n) :
    tmp = int(input())

    sum = 0
    n = 0

    for j in range(1, tmp+1) :
        for k in range(1, j+2) :
            n += k
        sum += j*n
        n = 0
    print(sum)