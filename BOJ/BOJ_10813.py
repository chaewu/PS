N, M = map(int, input().split())

ball_basket = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    ball_basket[i - 1], ball_basket[j - 1] = ball_basket[j - 1], ball_basket[i - 1]


print(*ball_basket)
