N = int(input())

num = []

for _ in range(N) :
    x,y = map(int, input().split())
    num.append([x,y])

num.sort(key = lambda x : (x[1], x[0]))

for i in num :
    print(i[0], i[1])
