N, M = map(int, input().split())
ball_basket = [0 for i in range(N)] # 크기 N의 리스트를 생성 및 0으로 값 초기화

# i에 시작 바구니 j에 끝 바구니, k에 넣을 값 적고 적어도 한 for문에서 공 넣고, for문 끝내기

for X in range(M):
    i, j, k = map(int, input().split())
    for Y in range(i - 1, j):
        ball_basket[Y] = k

print(*ball_basket)
