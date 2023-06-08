N = int(input())

li = []

for _ in range(N) :
    x, y = map(int,input().split())

    li.append([x,y])

li.sort(key = lambda x : (x[0], x[1]))

for i in range(N) :
    print(li[i][0], li[i][1])
