N, M = map(int, input().split())

ball_basket = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp_list = []
    for x in range(i - 1, j):
        tmp_list.append(ball_basket[x])
    tmp_list.reverse()

    change = 0
    for y in range(i - 1, j):
        ball_basket[y] = tmp_list[change]
        change += 1

print(*ball_basket)
